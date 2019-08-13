try:
    from ._version import version as __version__
except ImportError:
    try:
        import setuptools_scm
        __version__ = setuptools_scm.get_version(
            root="../../", relative_to=__file__,
            version_scheme="post-release", local_scheme="node-and-date")
    except (ImportError, LookupError):
        __version__ = "(unknown version)"


import importlib
from importlib.machinery import PathFinder
import logging
from pathlib import Path
import sys
import tokenize

import matplotlib as mpl


_log = logging.getLogger(__name__)


def _main():
    class MplBackendPathFinder(PathFinder):
        def find_spec(self, fullname, path, target=None):
            if path == __path__ and fullname.startswith(f"{__name__}."):
                _, rest = fullname.split(".", 1)
                for candidate in [f"matplotlib.backends.backend_{rest}", rest]:
                    spec = importlib.util.find_spec(candidate)
                    if spec is not None:

                        def exec_module(module):
                            sys.modules[f"{__name__}.{spec.name}"] = module
                            return type(spec.loader).exec_module(
                                spec.loader, module)

                        spec.loader.exec_module = exec_module
                        return spec
            return super().find_spec(fullname, path, target)

    sys.meta_path.append(MplBackendPathFinder())

    mplrcpy_path = Path(mpl.get_configdir(), "matplotlibrc.py")
    try:
        with tokenize.open(mplrcpy_path) as file:
            mplrcpy = file.read()
    except IOError:
        _log.warning(f"Failed to read {mplrcpy_path}; falling back to "
                     f"automatic backend selection.")
    else:
        exec(mplrcpy, {})


_main()
