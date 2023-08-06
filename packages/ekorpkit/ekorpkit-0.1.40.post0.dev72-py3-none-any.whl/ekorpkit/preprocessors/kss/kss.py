#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Korean Sentence Splitter
# Split Korean text into sentences using heuristic algorithm.
#
# Copyright (C) 2021 Hyun-Woong Ko <kevin.ko@tunib.ai> and Sang-Kil Park <skpark1224@hyundai.com>
# All rights reserved.
#
# This software may be modified and distributed under the terms
# of the BSD license.  See the LICENSE file for details.

import gc
import math
from typing import List, Union, Tuple
from .cache import LRUCache
from .morph import MorphExtractor

from .base import (
    Const,
    Eojeol,
    Postprocessor,
    Preprocessor,
    check_pos,
    do_push_pop_symbol,
    empty,
    length_constraints,
    get_chunk_with_index,
    preprocess_text,
    build_preprocessed_list,
)
from .rule import Table, Stats, ID

_morph = MorphExtractor()
# _cache = LRUCache(max_size=100)


class KSS:
    def __init__(
        self,
        use_heuristic: bool = False,
        use_quotes_brackets_processing: bool = False,
        max_recover_step: int = 5,
        max_recover_length: int = 20000,
        backend: str = "fugashi",
        dicdir=None,
        userdic_path=None,
        # disable_gc: bool = False,
        # cache_size: int = 1000,
        **kwargs,
    ) -> Union[List[str], List[List[str]]]:
        """
        Initialize KSS.

        Args:
                use_heuristic (bool): use heuristic algorithms or not
                use_quotes_brackets_processing (bool): use quotes or bracket processing or not
                max_recover_step (int): maximum step for quote and bracket misalignment recovering
                max_recover_length (int): maximum text length to recover when quote and bracket misaligned
                backend (str): max length of text to use morpheme feature
                disable_gc (bool): disable garbage collecting (It helps to improve speed)
        """
        assert isinstance(backend, str), "param `backend` must be `str` type"

        self.backend = backend.lower()

        assert self.backend in [
            "mecab-python3",
            "fugashi",
            "none",
        ], "Wrong backend! Currently, we support [`fugashi`, `mecab-python3`, `none`] backend."

        assert isinstance(
            use_heuristic, bool
        ), "param `use_heuristic` must be `bool` type"
        self.use_heuristic = use_heuristic
        assert isinstance(
            use_quotes_brackets_processing, bool
        ), "param `use_quotes_brackets_processing` must be `bool` type"
        self.use_quotes_brackets_processing = use_quotes_brackets_processing
        assert isinstance(
            max_recover_step, int
        ), "param `max_recover_step` must be `int` type"
        self.max_recover_step = max_recover_step
        assert isinstance(
            max_recover_length, int
        ), "param `max_recover_length` must be `int` type"
        self.max_recover_length = max_recover_length
        # assert isinstance(num_workers, int), "param `num_workers` must be `int` type"
        # self.num_workers = get_num_workers(num_workers)

        # self.disable_gc = disable_gc
        # if self.disable_gc:
        # 	gc.disable()
        _morph.parse_args(
            backend=self.backend, dicdir=dicdir, userdic_path=userdic_path
        )
        # if cache_size > 1:
        # 	_cache.max_size = cache_size

    def segment(
        self,
        text: str,
    ) -> List[str]:
        """
        Split document to sentences.

        Args:
                text (str): input text

        Returns:
                List[str]: list of segmented sentences
        """
        assert isinstance(text, str), "param `text` must be str."

        results = []

        self.max_recover_step = length_constraints(
            text,
            self.max_recover_length,
            self.max_recover_step,
        )

        preprocessed_list = build_preprocessed_list(text)
        if len(preprocessed_list) == 0:
            return results

        for t in preprocessed_list:
            results += self._split_into_sentences(
                text=t,
                use_heuristic=self.use_heuristic,
                use_quotes_brackets_processing=self.use_quotes_brackets_processing,
                max_recover_step=self.max_recover_step,
                max_recover_length=self.max_recover_length,
                backend=self.backend,
            )

        # if self.disable_gc:
        # 	gc.enable()

        return results

    def chunk(
        self,
        text: str,
        max_length: int,
        overlap: bool = False,
    ) -> List[str]:
        """
        Split chunks from input texts by max_length.

        Args:
                text (Union[str, List[str], tuple]): input texts
                max_length (int): max length of ecah chunk
                overlap (bool): whether allow duplicated sentence

        Returns:
                Union[List[str], List[List[str]]]: chunks of segmented sentences
        """

        assert isinstance(text, str), "param `text` must be str."
        assert isinstance(max_length, int), "param `max_length` must be `int` type."
        assert isinstance(overlap, bool), "param `overlap` must be `bool` type."

        span, chunks = [], []
        text = preprocess_text(text)

        for index in self._split_into_sentence_index(text):
            if len(span) > 0:
                if index[0] - span[0][1] > max_length:
                    chunks.append(get_chunk_with_index(text, span))
                    if overlap:
                        span = span[math.trunc(len(span) / 2) :]
                    else:
                        span = []

            span.append(index)
        chunks.append(get_chunk_with_index(text, span))
        return chunks

    def _split_into_sentence_index(self, text) -> List[Tuple[int, int]]:
        sentences = self.segment(text)
        offset, sentence_indice = 0, []

        for sentence in sentences:
            sentence_indice.append(
                (
                    offset + text.index(sentence),
                    offset + text.index(sentence) + len(sentence),
                )
            )
            offset += text.index(sentence) + len(sentence)
            text = text[text.index(sentence) + len(sentence) :]

        return sentence_indice

    def _split_into_sentences(
        self,
        text: str,
        use_heuristic: bool,
        use_quotes_brackets_processing: bool,
        max_recover_step: int,
        max_recover_length: int,
        backend: str,
        recover_step: int = 0,
    ):
        # _cache = self._cache
        # _morph = self._morph
        # if _cache is not None and text in _cache.dic:
        # 	return _cache.get(text)
        # else:
        # 	original_text = deepcopy(text)

        use_morpheme = backend != "none"
        prep = Preprocessor(use_morpheme=use_morpheme)
        post = Postprocessor()

        if not use_morpheme:
            # but if you use morpheme feature, it is unnecessary.
            text = prep.add_ec_cases_to_dict(text)

        text = prep.add_emojis_to_dict(text)
        text = prep.backup(text)

        for sent in Const.quotes_or_brackets:
            text = text.replace(sent, f"\u200b{sent}\u200b")

        if use_morpheme:
            eojeols = _morph.pos(text=text)
        else:
            eojeols = [Eojeol(t, "EF+ETN") for t in text]

        double_stack, single_stack, bracket_stack = [], [], []
        empty_stacks = lambda: empty([single_stack, double_stack, bracket_stack], dim=2)
        DA = Stats.DA_MORPH if use_morpheme else Stats.DA_EOJEOL

        results = []
        cur_sentence = []
        prev = Eojeol()
        prev_non_space = Eojeol()
        cur_stat = Stats.DEFAULT

        last_single_pos, single_quote_pop = 0, "'"
        last_double_pos, double_quote_pop = 0, '"'
        last_bracket_pos, bracket_pop = 0, " "

        for i, eojeol in enumerate(eojeols):
            if cur_stat == Stats.DEFAULT:
                if eojeol.eojeol in Const.double_quotes:
                    if use_quotes_brackets_processing:
                        if eojeol.eojeol in Const.double_quotes_open_to_close.keys():
                            double_quote_pop = do_push_pop_symbol(
                                double_stack,
                                Const.double_quotes_open_to_close[eojeol.eojeol],
                                eojeol.eojeol,
                            )
                        else:
                            double_quote_pop = do_push_pop_symbol(
                                double_stack,
                                Const.double_quotes_close_to_open[eojeol.eojeol],
                                eojeol.eojeol,
                            )
                        last_double_pos = i

                elif eojeol.eojeol in Const.single_quotes:
                    if use_quotes_brackets_processing:
                        if eojeol.eojeol in Const.single_quotes_open_to_close.keys():
                            single_quote_pop = do_push_pop_symbol(
                                single_stack,
                                Const.single_quotes_open_to_close[eojeol.eojeol],
                                eojeol.eojeol,
                            )
                        else:
                            single_quote_pop = do_push_pop_symbol(
                                single_stack,
                                Const.single_quotes_close_to_open[eojeol.eojeol],
                                eojeol.eojeol,
                            )
                        last_single_pos = i

                elif eojeol.eojeol in Const.brackets:
                    if use_quotes_brackets_processing:
                        if eojeol.eojeol in Const.bracket_open_to_close.keys():
                            bracket_pop = do_push_pop_symbol(
                                bracket_stack,
                                Const.bracket_open_to_close[eojeol.eojeol],
                                eojeol.eojeol,
                            )
                        else:
                            bracket_pop = do_push_pop_symbol(
                                bracket_stack,
                                Const.bracket_close_to_open[eojeol.eojeol],
                                eojeol.eojeol,
                            )
                        last_bracket_pos = i

                elif eojeol.eojeol in [".", "!", "?", "…", "~"]:
                    if (
                        (Table[Stats.SB][prev.eojeol] & ID.PREV)
                        and empty_stacks()
                        # check if pos is SF(마침표, 물음표, 느낌표) or SE(줄임표)
                    ):
                        if not use_morpheme:
                            cur_stat = Stats.SB
                        else:
                            if i != 0:
                                if check_pos(eojeols[i - 1], ["EF", "ETN"]):
                                    cur_stat = Stats.SB

                if use_heuristic is True:
                    if eojeol.eojeol in ["다"]:
                        if (
                            (Table[DA][prev.eojeol] & ID.PREV)
                            and check_pos(eojeol, ["EF"])
                            and empty_stacks()
                            # check if pos is EF(종결어미)
                        ):
                            if not use_morpheme:
                                if i != len(eojeols) - 1:
                                    if eojeols[i + 1].eojeol in Const.endpoint:
                                        cur_stat = DA
                            else:
                                cur_stat = DA

                    elif eojeol.eojeol in ["요"]:
                        if (
                            (Table[Stats.YO][prev.eojeol] & ID.PREV)
                            and check_pos(eojeol, ["EF"])
                            and empty_stacks()
                            # check if pos is EF(종결어미)
                        ):
                            if not use_morpheme:
                                if i != len(eojeols) - 1:
                                    if eojeols[i + 1].eojeol in Const.endpoint:
                                        cur_stat = Stats.YO
                            else:
                                cur_stat = Stats.YO

                    elif eojeol.eojeol in ["죠", "쥬", "죵"]:
                        if (
                            (Table[Stats.JYO][prev.eojeol] & ID.PREV)
                            and check_pos(eojeol, ["EF"])
                            and empty_stacks()
                            # check if pos is EF 종결어미
                        ):
                            if not use_morpheme:
                                if i != len(eojeols) - 1:
                                    if eojeols[i + 1].eojeol in Const.endpoint:
                                        cur_stat = Stats.JYO
                            else:
                                cur_stat = Stats.JYO
                    elif use_morpheme:
                        if (
                            empty_stacks()
                            and i != len(eojeols) - 1
                            and check_pos(eojeol, ["ETN", "EF"])
                            and check_pos(eojeols[i + 1], ["SP", "SE", "SF"])
                            and not check_pos(
                                eojeol, ["J", "XS"]
                            )  # ETN+XSN 같은 케이스 막기위해
                            and eojeol.eojeol
                            not in [
                                "다",
                                "요",
                                "죠",
                                "기",
                            ]  # ~ 하기 (명사파생 접미사가 전성어미로 오해되는 경우)
                        ):
                            cur_stat = Stats.EOMI
                            # 일반적으로 적용할 수 있는 어미세트 NEXT 세트 적용.
            else:
                if eojeol.eojeol in Const.double_quotes:
                    last_double_pos = i

                elif eojeol.eojeol in Const.single_quotes:
                    last_single_pos = i

                elif eojeol.eojeol in Const.brackets:
                    last_bracket_pos = i

                endif = False
                if not endif:
                    # Space
                    if (
                        eojeol.eojeol == " "
                        or Table[Stats.COMMON][eojeol.eojeol] & ID.CONT
                    ):
                        if Table[cur_stat][prev.eojeol] & ID.NEXT1:
                            results.append(cur_sentence)
                            cur_sentence = [prev]
                            cur_stat = Stats.DEFAULT
                        endif = True

                if not endif:
                    if Table[cur_stat][eojeol.eojeol] & ID.NEXT:
                        if Table[cur_stat][prev.eojeol] & ID.NEXT1:
                            # NEXT1 + NEXT => 자르지 않는다.
                            cur_sentence.append(prev)

                        elif prev_non_space.eojeol in Table[Stats.COMMON]:
                            # NEW RULE for KSS 3 to fix following issue.
                            # https://github.com/hyunwoongko/kss/issues/7

                            if not check_pos(eojeol, ["EC", "VC"]):
                                # "말했다. 고한다." => 고(EC): not segment
                                # "말했다. 고구려는" => 고(NNG): segment
                                results.append(cur_sentence)
                                cur_sentence = []

                        cur_stat = Stats.DEFAULT
                        endif = True

                if not endif:
                    if Table[cur_stat][eojeol.eojeol] & ID.NEXT1:
                        if Table[cur_stat][prev.eojeol] & ID.NEXT1:
                            # NEXT1 + NEXT1 => 자른다.
                            results.append(cur_sentence)
                            cur_sentence = [prev]
                            cur_stat = Stats.DEFAULT
                        endif = True

                if not endif:
                    if Table[cur_stat][eojeol.eojeol] & ID.NEXT2:
                        if Table[cur_stat][prev.eojeol] & ID.NEXT1:
                            # NEXT1 + NEXT2 => 자르지 않는다.
                            cur_sentence.append(prev)
                        else:
                            # "말했다. 고한다." => 고(EC): not segmentt
                            # "말했다. 고구려는" => 고(NNG): segment
                            if not check_pos(eojeol, ["EC"]):
                                # NOT(NEXT1) + NEXT2 => 자른다.
                                results.append(cur_sentence)
                                cur_sentence = []

                        cur_stat = Stats.DEFAULT
                        endif = True

                if not endif:
                    if (
                        not Table[cur_stat][eojeol.eojeol]
                        or Table[cur_stat][eojeol.eojeol] & ID.PREV
                    ):  # NOT exists

                        if eojeol.eojeol not in Const.not_endpoint:
                            results.append(cur_sentence)
                            cur_sentence = []
                            if Table[cur_stat][prev.eojeol] & ID.NEXT1:
                                cur_sentence.append(prev)

                        cur_stat = Stats.DEFAULT

                        if eojeol.eojeol in Const.double_quotes:
                            if use_quotes_brackets_processing:
                                if (
                                    eojeol.eojeol
                                    in Const.double_quotes_open_to_close.keys()
                                ):
                                    double_quote_pop = do_push_pop_symbol(
                                        double_stack,
                                        Const.double_quotes_open_to_close[
                                            eojeol.eojeol
                                        ],
                                        eojeol.eojeol,
                                    )
                                else:
                                    double_quote_pop = do_push_pop_symbol(
                                        double_stack,
                                        Const.double_quotes_close_to_open[
                                            eojeol.eojeol
                                        ],
                                        eojeol.eojeol,
                                    )

                        elif eojeol.eojeol in Const.single_quotes:
                            if use_quotes_brackets_processing:
                                if (
                                    eojeol.eojeol
                                    in Const.single_quotes_open_to_close.keys()
                                ):
                                    single_quote_pop = do_push_pop_symbol(
                                        single_stack,
                                        Const.single_quotes_open_to_close[
                                            eojeol.eojeol
                                        ],
                                        eojeol.eojeol,
                                    )
                                else:
                                    single_quote_pop = do_push_pop_symbol(
                                        single_stack,
                                        Const.single_quotes_close_to_open[
                                            eojeol.eojeol
                                        ],
                                        eojeol.eojeol,
                                    )

                        elif eojeol.eojeol in Const.brackets:
                            if use_quotes_brackets_processing:
                                if eojeol.eojeol in Const.bracket_open_to_close.keys():
                                    bracket_pop = do_push_pop_symbol(
                                        bracket_stack,
                                        Const.bracket_open_to_close[eojeol.eojeol],
                                        eojeol.eojeol,
                                    )
                                else:
                                    bracket_pop = do_push_pop_symbol(
                                        bracket_stack,
                                        Const.bracket_close_to_open[eojeol.eojeol],
                                        eojeol.eojeol,
                                    )

            if cur_stat == Stats.DEFAULT or not (
                Table[cur_stat][eojeol.eojeol] & ID.NEXT1
            ):
                cur_sentence.append(eojeol)

            prev = eojeol

            if eojeol.eojeol != " ":
                prev_non_space = eojeol

        if not empty(cur_sentence, dim=1):
            results.append(cur_sentence)
            cur_sentence = []

        if Table[cur_stat][prev.eojeol] & ID.NEXT1:
            cur_sentence.append(prev)
            results.append(cur_sentence)

        results = prep.tostring(results)

        if use_heuristic is True:
            results = post.apply_heuristic(text, results, use_morpheme)

        kwargs = {
            "use_heuristic": use_heuristic,
            "use_quotes_brackets_processing": use_quotes_brackets_processing,
            "max_recover_step": max_recover_step,
            "max_recover_length": max_recover_length,
            "backend": backend,
            "recover_step": recover_step + 1,
        }

        if recover_step < max_recover_step:
            if len(single_stack) != 0:
                results = self._realign_by_quotes(
                    text,
                    last_single_pos,
                    single_quote_pop,
                    **kwargs,
                )
            if len(double_stack) != 0:
                results = self._realign_by_quotes(
                    text,
                    last_double_pos,
                    double_quote_pop,
                    **kwargs,
                )
            if len(bracket_stack) != 0:
                results = self._realign_by_quotes(
                    text,
                    last_bracket_pos,
                    bracket_pop,
                    **kwargs,
                )

        outputs = []
        for sent in results:
            sent = prep.restore(sent)
            sent = sent.replace("\u200b", "")
            sent = sent.strip()
            if len(sent) > 0:
                outputs.append(sent)

        # if _cache is not None:
        # 	_cache.put(original_text, outputs)

        return outputs

    def _realign_by_quotes(self, text, last_quote_pos, quote_type, **kwargs):
        before_quote = self._split_into_sentences(text[:last_quote_pos], **kwargs)
        before_last = before_quote[-1] if len(before_quote) > 0 else ""
        before_quote = [] if len(before_quote) == 1 else before_quote[:-1]

        after_quote = self._split_into_sentences(text[last_quote_pos + 1 :], **kwargs)
        after_first = after_quote[0] if len(after_quote) > 0 else ""
        after_quote = [] if len(after_quote) == 1 else after_quote[1:]

        middle_quote = [before_last + quote_type + after_first]
        return before_quote + middle_quote + after_quote
