import typing as t
import urllib.parse

from .lexicon import Lex

from .caller import WebCaller

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
        route: t.Text ="americas",
        load: bool = True
    ):
        self.key = key
        self.route = route
        self.locale = locale
        self.region = region
        self.handle = WebCaller(key, locale, region, route)

        if load:
            self.get_content(cache=True)
    
    def _content_if_cache(self):
        return getattr(self, "content", self.get_content())

    def __getattribute__(self, name):
        return super(Client, self).__getattribute__(name)

    def get_content(self, cache: bool = True) -> ContentDTO:
        content = ContentDTO(self.handle.call("GET", "content"))

        if cache:
            self.content = content
        
        return content
    
    def asset(self, **kw: t.Mapping):
        if len(kw) > 1: raise ValueError

        key = str(list(kw.keys())[0])
        value = kw[key]

        if key == "assetName":
            genexpr = lambda m: value.endswith(m[key])
        else:
            genexpr = lambda m: m[key] == value
        
        for name in Lex.CONTENT_NAMES:
            for asset in getattr(self.content, name):
                try:
                    if genexpr(asset):
                        return ContentItemDTO(asset)
                except KeyError:
                    pass
    
        return None

    def get_user_by_puuid(self, puuid: t.Text) -> AccountDTO:
        """Get a Riot AccountDTO by the given PUUID."""
        r = self.handle.call("GET", "puuid", puuid=puuid)

        return AccountDTO(r, self.handle)

    def get_user_by_name(self, name: t.Text) -> AccountDTO:
        """Get a Riot AccountDTO by a given name and tag."""
        vals = name.split("#")
        vals = [urllib.parse.quote(v, safe=Lex.SAFES) for v in vals]
        r = self.handle.call("GET", "game-name", route=True, name=vals[0], tag=vals[1])

        return AccountDTO(r, self.handle)

    def get_platform_status(self) -> PlatformDataDTO:
        """Get the current platform status for Valorant."""
        r = self.handle.call("GET", "status")

        return PlatformDataDTO(r)

    def get_acts(self) -> t.Iterable[ActDTO]:
        """Get a ContentList of Acts from Valorant."""
        content = self._content_if_cache()
        acts = [ActDTO(a) for a in content.acts]

        return ContentList(acts)

    def get_characters(self) -> t.Iterable[ContentItemDTO]:
        """Get a ContentList of Agents from Valorant."""
        content = self._content_if_cache()
        characters = [ContentItemDTO(c) for c in content.characters]

        return ContentList(characters)

    def get_current_act(self) -> t.Optional[ActDTO]:
        """Get the current Act (indiscriminate of episode)."""
        for act in self.get_acts():
            if act.isActive:
                return act

        return None

    def get_charms(self) -> ContentList:
        """Get a ContentList of Gun Buddies from Valorant."""
        content = self._content_if_cache()
        charms = [ContentItemDTO(c) for c in content.charms]

        return ContentList(charms)

    def get_charm_levels(self) -> ContentList:
        """Get a ContentList of Gun Buddy Levels from Valorant."""
        content = self._content_if_cache()
        charmLevels = [ContentItemDTO(c) for c in content.charmLevels]

        return ContentList(charmLevels)

    def get_chromas(self) -> ContentList:
        content = self._content_if_cache()
        chromas = [ContentItemDTO(c) for c in content.chromas]

        return ContentList(chromas)

    def get_equips(self) -> ContentList:
        content = self._content_if_cache()
        equips = [ContentItemDTO(e) for e in content.equips]

        return ContentList(equips)

    def get_leaderboard(self, size: int = 100, page: int = 0, actID: str = ""):
        """Get the top user's in your client's region during a given Act."""
        actID = self.get_current_act().id if not actID else actID
        params = {"size": size, "startIndex": size * page}

        r = self.handle.call("GET", "leaderboard", params=params, actID=actID)

        return LeaderboardDTO(r)

    def get_maps(self) -> ContentList:
        """Get a ContentList of Maps from Valorant."""
        content = self._content_if_cache()
        maps = [ContentItemDTO(m) for m in content.maps]

        return ContentList(maps)

    def get_skins(self) -> ContentList:
        """Get a ContentList of Weapon Skins from Valorant."""
        content = self._content_if_cache()
        skins = [ContentItemDTO(s) for s in content.skins]

        return ContentList(skins)

    def get_skin_levels(self) -> ContentList:
        """Get a ContentList of Weapon Skin Levels from Valorant."""
        content = self._content_if_cache()
        skinLevels = [ContentItemDTO(s) for s in content.skinLevels]

        return ContentList(skinLevels)

    def get_game_modes(self) -> ContentList:
        """Get a ContentList of Game Modes from Valorant."""
        content = self._content_if_cache()
        gameModes = [ContentItemDTO(g) for g in content.gameModes]

        return ContentList(gameModes)

    def get_sprays(self) -> ContentList:
        """Get a ContentList of Sprays from Valorant."""
        content = self._content_if_cache()
        sprays = [ContentItemDTO(s) for s in content.sprays]

        return ContentList(sprays)

    def get_spray_levels(self) -> ContentList:
        """Get a ContentList of Spray Levels from Valorant."""
        content = self._content_if_cache()
        sprayLevels = [ContentItemDTO(s) for s in content.sprayLevels]

        return ContentList(sprayLevels)

    def get_player_cards(self) -> ContentList:
        """Get a ContentList of Player Cards from Valorant."""
        content = self._content_if_cache()
        playerCards = [ContentItemDTO(p) for p in content.playerCards]

        return ContentList(playerCards)

    def get_player_titles(self) -> ContentList:
        """Get a ContentList of Player Titles from Valorant."""
        content = self._content_if_cache()
        playerTitles = [ContentItemDTO(p) for p in content.playerTitles]

        return ContentList(playerTitles)
