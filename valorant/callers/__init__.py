import aiohttp
import requests
import typing as t

from .async_ import AsyncCaller
from .sync import WebCaller

SessionType = t.Union[requests.Session, aiohttp.ClientSession]
CallerType = t.Union[AsyncCaller, WebCaller]

__all__ = ["AsyncCaller", "CallerType", "SessionType", "WebCaller"]
