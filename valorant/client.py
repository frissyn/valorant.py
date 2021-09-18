import urllib.parse

from .caller import WebCaller

from .objects import ActDTO
from .objects import AccountDTO
from .objects import ContentItemDTO
from .objects import LeaderboardDTO
from .objects import PlatformDataDTO

from .objects import ContentList

from .values import SAFES
from .values import LOCALE


def update(stale: dict, latest: dict) -> dict:
    for key, items in latest.items():
        stale[key] = latest[key]

    return stale


class Client(object):
    def __init__(self, key, locale=LOCALE, region="na", route="americas", reload=True):
        self.key = key
        self.route = route
        self.locale = locale
        self.region = region
        self.handle = WebCaller(key, locale, region, route)

        if reload:
            self.reload()
        else:
            pass

    def __getattribute__(self, name):
        return super(Client, self).__getattribute__(name)

    def set_attributes(self, attrs) -> None:
        for attr, value in attrs.items():
            self.__setattr__(attr, value)

        return

    def reload(self) -> None:
        """Reload the current cached response for the VAL-CONTENT endpoints."""
        r = self.handle.call("GET", "content")
        self.set_attributes(r)

        return

    def get_user_by_puuid(self, puuid: str) -> AccountDTO:
        """Get a Riot account by the given PUUID."""
        r = self.handle.call("GET", "puuid", puuid=puuid)

        return AccountDTO(r)

    def get_user_by_name(self, name: str) -> AccountDTO:
        """Get a Riot account by a given name and tag."""
        vals = name.split("#")
        vals = [urllib.parse.quote(v, safe=SAFES) for v in vals]
        r = self.handle.call("GET", "game-name", route=True, name=vals[0], tag=vals[1])

        return AccountDTO(r)

    def get_platform_status(self) -> PlatformDataDTO:
        """Get the current platform status for Valorant."""
        r = self.handle.call("GET", "status")

        return PlatformDataDTO(r)

    def get_acts(self) -> ContentList:
        """Get a ContentList of Acts from Valorant."""
        acts = [ActDTO(a) for a in self.acts]

        return ContentList(acts)

    def get_characters(self) -> ContentList:
        """Get a ContentList of Agents from Valorant."""
        characters = [ContentItemDTO(c) for c in self.characters]

        return ContentList(characters)

    def get_current_act(self) -> ActDTO:
        """Get the current Act (indiscriminate of episode)."""
        for act in self.get_acts():
            if act.isActive and "ACT" in act.name:
                return act
            else:
                continue

        return None

    def get_charms(self) -> ContentList:
        """Get a ContentList of Gun Buddies from Valorant."""
        charms = [ContentItemDTO(c) for c in self.charms]

        return ContentList(charms)

    def get_charm_levels(self) -> ContentList:
        """Get a ContentList of Gun Buddy Levels from Valorant."""
        charmLevels = [ContentItemDTO(c) for c in self.charmLevels]

        return ContentList(charmLevels)

    def get_chromas(self) -> ContentList:
        chromas = [ContentItemDTO(c) for c in self.chromas]

        return ContentList(chromas)

    def get_equips(self) -> ContentList:
        equips = [ContentItemDTO(e) for e in self.equips]

        return ContentList(equips)

    def get_leaderboard(self, size: int = 100, page: int = 0, actID: str = ""):
        """Get the top user's in your client's region during a given Act."""
        actID = self.get_current_act().id if not actID else actID
        params = {"size": size, "startIndex": size * page}

        r = self.handle.call("GET", "leaderboard", params=params, actID=actID)

        return LeaderboardDTO(r)

    def get_maps(self) -> ContentList:
        """Get a ContentList of Maps from Valorant."""
        maps = [ContentItemDTO(m) for m in self.maps]

        return ContentList(maps)

    def get_skins(self) -> ContentList:
        """Get a ContentList of Weapon Skins from Valorant."""
        skins = [ContentItemDTO(s) for s in self.skins]

        return ContentList(skins)

    def get_skin_levels(self) -> ContentList:
        """Get a ContentList of Weapon Skin Levels from Valorant."""
        skinLevels = [ContentItemDTO(s) for s in self.skinLevels]

        return ContentList(skinLevels)

    def get_game_modes(self) -> ContentList:
        """Get a ContentList of Game Modes from Valorant."""
        gameModes = [ContentItemDTO(g) for g in self.gameModes]

        return ContentList(gameModes)

    def get_sprays(self) -> ContentList:
        """Get a ContentList of Sprays from Valorant."""
        sprays = [ContentItemDTO(s) for s in self.sprays]

        return ContentList(sprays)

    def get_spray_levels(self) -> ContentList:
        """Get a ContentList of Spray Levels from Valorant."""
        sprayLevels = [ContentItemDTO(s) for s in self.sprayLevels]

        return ContentList(sprayLevels)

    def get_player_cards(self) -> ContentList:
        """Get a ContentList of Player Cards from Valorant."""
        playerCards = [ContentItemDTO(p) for p in self.playerCards]

        return ContentList(playerCards)

    def get_player_titles(self) -> ContentList:
        """Get a ContentList of Player Titles from Valorant."""
        playerTitles = [ContentItemDTO(p) for p in self.playerTitles]

        return ContentList(playerTitles)
