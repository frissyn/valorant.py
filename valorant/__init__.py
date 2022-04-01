import typing as t

from .client import Client
from .lexicon import Lex
from .local import LocalClient
from .objects import *
from .query import exp, Expression


__title__ = "valorant"
__author__ = "frissyn"
__all__ = ["Client", "exp", "Expression", "LocalClient", "Lex"]


class Version(t.NamedTuple):
    major: int
    minor: int
    micro: int
    release: t.Literal["alpha", "beta", "dev"]


version_info = Version(major=1, minor=0, micro=2, release="dev")

tag = f"-{version_info.release}" if version_info.release else ""
__version__ = ".".join(str(i) for i in version_info[:3]) + tag
