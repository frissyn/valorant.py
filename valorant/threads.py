import asyncio
import typing as t

from .lexicon import Lex

from .client import Client

from .caller import WebCaller

from .objects import ActDTO
from .objects import ContentDTO
from .objects import AccountDTO
from .objects import ContentList
from .objects import ContentItemDTO
from .objects import PlatformDataDTO


class AsyncClient(Client):
    def __init__(
        self,
        key: t.Text,
        locale: t.Optional[t.Text] = Lex.LOCALE,
        region: t.Text = "na",
        route: t.Text = "americas",
        load_content: bool = True,
    ):
        self.key = key
        self.route = route
        self.locale = locale
        self.region = region
        self.handle = WebCaller(key, locale, region, route)

        if load_content:
            asyncio.run(self.get_content(cache=True))
        else:
            self.content = None

    def _content_if_cache(self):
        content = getattr(self, "content", None)

        return content if content else asyncio.run(self.get_content())

    def __getattribute__(self, name):
        return super(AsyncClient, self).__getattribute__(name)

    async def get_content(self, cache: bool = True) -> ContentDTO:
        return super().get_content(cache=cache)

    async def get_user(self, puuid: t.Text) -> AccountDTO:
        return super().get_user(puuid)

    async def get_user_by_name(self, name: t.Text) -> AccountDTO:
        return super().get_user_by_name(name)

    async def get_platform_status(self) -> PlatformDataDTO:
        return super().get_platform_status()

    async def get_acts(self) -> t.List[ActDTO]:
        return super().get_acts()

    async def get_characters(self) -> t.List[ContentItemDTO]:
        return super().get_characters()

    async def get_current_act(self) -> t.Optional[ActDTO]:
        return super().get_current_act()

    async def get_charms(self) -> ContentList:
        return super().get_charms()

    async def get_charm_levels(self) -> ContentList:
        return super().get_charm_levels()

    async def get_chromas(self) -> ContentList:
        return super().get_chromas()

    async def get_equips(self) -> ContentList:
        return super().get_equips()

    async def get_leaderboard(self, size: int = 100, page: int = 0, actID: t.Text = ""):
        return super().get_leaderboard(size=size, page=page, actID=actID)

    async def get_maps(self) -> ContentList:
        return super().get_maps()

    async def get_skins(self) -> ContentList:
        return super().get_skins()

    async def get_skin_levels(self) -> ContentList:
        return super().get_skin_levels()

    async def get_game_modes(self) -> ContentList:
        return super().get_game_modes()

    async def get_sprays(self) -> ContentList:
        return super().get_sprays()

    async def get_spray_levels(self) -> ContentList:
        return super().get_spray_levels()

    async def get_player_cards(self) -> ContentList:
        return super().get_player_cards()

    async def get_player_titles(self) -> ContentList:
        return super().get_player_titles()
