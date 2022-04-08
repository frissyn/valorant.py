import typing as t
import urllib.parse

from .lexicon import Lex

from .callers import AsyncCaller

from .objects import (
    DTO,
    ActDTO,
    AccountDTO,
    ContentDTO,
    ContentItemDTO,
    LeaderboardDTO,
    LeaderboardIterator,
    PlatformDataDTO,
    MatchDTO,
)


class AsyncClient(object):
    def __init__(
        self,
        key: t.Text,
        locale: t.Optional[t.Text] = Lex.LOCALE,
        region: t.Text = "na",
        route: t.Text = "americas",
    ):
        self.key = key
        self.route = route
        self.locale = locale
        self.region = region
        self.handle = AsyncCaller(key, locale=locale, region=region, route=route)

    async def _content_from_cache(self, from_cache=True):
        if from_cache and getattr(self, "content", False):
            return self.content
        else:
            self.content = ContentDTO(await self.handle.call("GET", "content"))

            return self.content

    async def get_content(self, cache: bool=False) -> ContentDTO:
        return await self._content_from_cache(from_cache=cache)
