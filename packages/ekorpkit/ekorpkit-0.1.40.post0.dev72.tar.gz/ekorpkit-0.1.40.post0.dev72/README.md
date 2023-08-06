# ekorpkit 【iːkɔːkɪt】 : **eKo**nomic **R**esearch **P**ython Tool**kit**

[![PyPI version](https://badge.fury.io/py/ekorpkit.svg)](https://badge.fury.io/py/ekorpkit) [![Jupyter Book Badge](https://jupyterbook.org/en/stable/_images/badge.svg)](https://entelecheia.github.io/ekorpkit-book/) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6497226.svg)](https://doi.org/10.5281/zenodo.6497226) [![release](https://github.com/entelecheia/ekorpkit/actions/workflows/release.yaml/badge.svg)](https://github.com/entelecheia/ekorpkit/actions/workflows/release.yaml) [![CodeQL](https://github.com/entelecheia/ekorpkit/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/entelecheia/ekorpkit/actions/workflows/codeql-analysis.yml) [![test](https://github.com/entelecheia/ekorpkit/actions/workflows/test.yaml/badge.svg)](https://github.com/entelecheia/ekorpkit/actions/workflows/test.yaml) [![CircleCI](https://circleci.com/gh/entelecheia/ekorpkit/tree/main.svg?style=shield)](https://circleci.com/gh/entelecheia/ekorpkit/tree/main) [![codecov](https://codecov.io/gh/entelecheia/ekorpkit/branch/main/graph/badge.svg?token=8I4ORHRREL)](https://codecov.io/gh/entelecheia/ekorpkit) [![markdown-autodocs](https://github.com/entelecheia/ekorpkit/actions/workflows/markdown-autodocs.yaml/badge.svg)](https://github.com/entelecheia/ekorpkit/actions/workflows/markdown-autodocs.yaml)

eKorpkit provides a flexible interface for NLP and ML research pipelines such as extraction, transformation, tokenization, training, and visualization. Its powerful config composition is backed by [Hydra](https://hydra.cc/).

## Key features

### Easy Configuration

- You can compose your configuration dynamically, enabling you to easily get the perfect configuration for each research. 
- You can override everything from the command line, which makes experimentation fast, and removes the need to maintain multiple similar configuration files. 
- With a help of the **eKonf** class, it is also easy to compose configurations in a jupyter notebook environment.

### No Boilerplate

- eKorpkit lets you focus on the problem at hand instead of spending time on boilerplate code like command line flags, loading configuration files, logging etc.

### Workflows

- A workflow is a configurable automated process that will run one or more jobs.
- You can divide your research into several unit jobs (tasks), then combine those jobs into one workflow.
- You can have multiple workflows, each of which can perform a different set of tasks.

### Sharable and Reproducible

- With eKorpkit, you can easily share your datasets and models.
- Sharing configs along with datasets and models makes every research reproducible.
- You can share each unit jobs or an entire workflow.

### Pluggable Architecture

- eKorpkit has a pluggable architecture, enabling it to combine with your own implementation.

## [Tutorials](https://entelecheia.github.io/ekorpkit-book)

Tutorials for [ekorpkit](https://github.com/entelecheia/ekorpkit) package can be found at https://entelecheia.github.io/ekorpkit-book/

## [Installation](https://entelecheia.github.io/ekorpkit-book/docs/basics/install.html)

Install the latest version of ekorpkit:

```bash
pip install ekorpkit
```

To install all extra dependencies,

```bash
pip install ekorpkit[all]
```

## [The eKorpkit Corpus](https://github.com/entelecheia/ekorpkit/blob/main/docs/corpus/README.md)

The eKorpkit Corpus is a large, diverse, bilingual (ko/en) language modelling dataset.

![ekorpkit corpus](https://github.com/entelecheia/ekorpkit/blob/main/docs/figs/ekorpkit_corpus.png?raw=true)

## Citation

```tex
@software{lee_2022_6497226,
  author       = {Young Joon Lee},
  title        = {eKorpkit: eKonomic Research Python Toolkit},
  month        = apr,
  year         = 2022,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.6497226},
  url          = {https://doi.org/10.5281/zenodo.6497226}
}
```

```tex
@software{lee_2022_ekorpkit,
  author       = {Young Joon Lee},
  title        = {eKorpkit: eKonomic Research Python Toolkit},
  month        = apr,
  year         = 2022,
  publisher    = {GitHub},
  url          = {https://github.com/entelecheia/ekorpkit}
}
```

## License

- eKorpkit is licensed under the [MIT License](https://opensource.org/licenses/MIT). This license covers the eKorpkit package and all of its components.
- Each corpus adheres to its own license policy. Please check the license of the corpus before using it!
