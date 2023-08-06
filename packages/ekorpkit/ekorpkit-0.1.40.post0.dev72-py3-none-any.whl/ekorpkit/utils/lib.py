import logging
import os
import subprocess
import sys
import importlib
from pathlib import Path
from ekorpkit.base import _is_dir, _is_file


log = logging.getLogger(__name__)


def gitclone(url, targetdir=None, verbose=False):
    if targetdir:
        res = subprocess.run(
            ["git", "clone", url, targetdir], stdout=subprocess.PIPE
        ).stdout.decode("utf-8")
    else:
        res = subprocess.run(
            ["git", "clone", url], stdout=subprocess.PIPE
        ).stdout.decode("utf-8")
    if verbose:
        print(res)
    else:
        log.info(res)


def pip(
    name,
    upgrade=False,
    prelease=False,
    editable=False,
    quiet=True,
    find_links=None,
    requirement=None,
    force_reinstall=False,
    verbose=False,
    **kwargs,
):
    _cmd = ["pip", "install"]
    if upgrade:
        _cmd.append("--upgrade")
    if prelease:
        _cmd.append("--pre")
    if editable:
        _cmd.append("--editable")
    if quiet:
        _cmd.append("--quiet")
    if find_links:
        _cmd += ["--find-links", find_links]
    if requirement:
        _cmd.append("--requirement")
    if force_reinstall:
        _cmd.append("--force-reinstall")
    for k in kwargs:
        k = k.replace("_", "-")
        _cmd.append(f"--{k}")
    _cmd.append(name)
    if verbose:
        log.info(f"Installing: {' '.join(_cmd)}")
    res = subprocess.run(_cmd, stdout=subprocess.PIPE).stdout.decode("utf-8")
    if verbose:
        print(res)
    else:
        log.info(res)


def pipi(name, verbose=False):
    res = subprocess.run(
        ["pip", "install", name], stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    if verbose:
        print(res)
    else:
        log.info(res)


def pipie(name, verbose=False):
    res = subprocess.run(
        ["git", "install", "-e", name], stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    if verbose:
        print(res)
    else:
        log.info(res)


def apti(name, verbose=False):
    res = subprocess.run(
        ["apt", "install", name], stdout=subprocess.PIPE
    ).stdout.decode("utf-8")
    if verbose:
        print(res)
    else:
        log.info(res)


def load_module_from_file(name, libpath, specname=None):
    module_path = os.path.join(libpath, name.replace(".", os.path.sep))
    if _is_file(module_path + ".py"):
        module_path = module_path + ".py"
    else:
        if _is_dir(module_path):
            module_path = os.path.join(module_path, "__init__.py")
        else:
            module_path = str(Path(module_path).parent / "__init__.py")

    spec = importlib.util.spec_from_file_location(name, module_path)
    module = importlib.util.module_from_spec(spec)
    if not specname:
        specname = spec.name
    sys.modules[specname] = module
    spec.loader.exec_module(module)


def ensure_import_module(name, libpath, liburi, specname=None, syspath=None):
    try:
        if specname:
            importlib.import_module(specname)
        else:
            importlib.import_module(name)
        log.info(f"{name} imported")
    except ImportError:
        if not os.path.exists(libpath):
            log.info(f"{libpath} not found, cloning from {liburi}")
            gitclone(liburi, libpath)
        if not syspath:
            syspath = libpath
        if syspath not in sys.path:
            sys.path.append(syspath)
        load_module_from_file(name, syspath, specname)
        specname = specname or name
        log.info(f"{name} not imported, loading from {syspath} as {specname}")
