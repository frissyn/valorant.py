import typing as t
import urllib.parse

from .lexicon import Lex

from .caller import WebCaller

from .objects import DTO
from .objects import ActDTO
from .objects import AccountDTO
from .objects import ContentDTO
from .objects import ContentList
from .objects import ContentItemDTO
from .objects import LeaderboardDTO
from .objects import PlatformDataDTO


class Client(object):
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
            self.get_content(cache=True)
        else:
            self.content = None

    def _content_if_cache(self):
        content = getattr(self, "content", None)

        return content if content else self.get_content()

    def __getattribute__(self, name):
        return super(Client, self).__getattribute__(name)

    def get_content(self, cache: bool = True) -> ContentDTO:
        content = ContentDTO(self.handle.call("GET", "content"))

        if cache:
            self.content = content

        return content

    def asset(self, **attributes: t.Mapping) -> t.Optional[DTO]:
        checks = 0

        for name in Lex.CONTENT_NAMES:
            for item in getattr(self._content_if_cache(), name):
                for attr, value in attributes.items():
                    if attr == "assetName":
                        genexpr = lambda m: value.endswith(getattr(item, attr))
                    else:
                        genexpr = lambda m: getattr(item, attr) == value

                    try:
                        if genexpr(item):
                            checks += 1
                    except AttributeError:
                        pass

                if checks == len(attributes):
                    return item
                else:
                    checks = 0

    def get_user(self, puuid: t.Text) -> AccountDTO:
        r = self.handle.call("GET", "puuid", puuid=puuid)

        return AccountDTO(r, self.handle)

    def get_user_by_name(self, name: t.Text) -> AccountDTO:
        vals = name.split("#")
        vals = [urllib.parse.quote(v, safe=Lex.SAFES) for v in vals]
        r = self.handle.call("GET", "game-name", route=True, name=vals[0], tag=vals[1])

        return AccountDTO(r, self.handle)

    def get_platform_status(self) -> PlatformDataDTO:
        r = self.handle.call("GET", "status")

        return PlatformDataDTO(r)

    def get_acts(self) -> t.Iterable[ActDTO]:
        return self._content_if_cache().acts

    def get_characters(self) -> t.Iterable[ContentItemDTO]:
        return self._content_if_cache().characters

    def get_current_act(self) -> t.Optional[ActDTO]:
        for act in self.get_acts():
            if act.isActive:
                return act

        return None

    def get_charms(self) -> ContentList:
        return self._content_if_cache().charms

    def get_charm_levels(self) -> ContentList:
        return self._content_if_cache().charmLevels

    def get_chromas(self) -> ContentList:
        return self._content_if_cache().chromas

    def get_equips(self) -> ContentList:
        return self._content_if_cache().equips

    def get_leaderboard(self, size: int = 100, page: int = 0, actID: t.Text = ""):
        actID = self.get_current_act().id if not actID else actID
        params = {"size": size, "startIndex": size * page}

        r = self.handle.call("GET", "leaderboard", params=params, actID=actID)

        return LeaderboardDTO(r)

    def get_maps(self) -> ContentList:
        return self._content_if_cache().maps

    def get_skins(self) -> ContentList:
        return self._content_if_cache().skins

    def get_skin_levels(self) -> ContentList:
        return self._content_if_cache().get_skin_levels

    def get_game_modes(self) -> ContentList:
        return self._content_if_cache().gameModes

    def get_sprays(self) -> ContentList:
        return self._content_if_cache().sprays

    def get_spray_levels(self) -> ContentList:
        return self._content_if_cache().sprayLevels

    def get_player_cards(self) -> ContentList:
        return self._content_if_cache().playerCards

    def get_player_titles(self) -> ContentList:
        return self._content_if_cache().playerTitles
