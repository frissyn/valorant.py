import requests
import urllib.parse

from .objects import ActDTO
from .objects import AccountDTO
from .objects import ContentItemDTO
from .objects import LeaderboardDTO
from .objects import PlatformDataDTO

from .objects import ContentList

from .values import SAFES
from .values import ROUTES
from .values import LOCALE
from .values import LOCALES
from .values import REGIONS
from .values import HEADERS
from .values import WEB_API
from .values import ENDPOINTS
from .values import CLIENT_API


def update(stale: dict, latest: dict) -> dict:
    for key, items in latest.items():
        stale[key] = latest[key]

    return stale


class Client(object):
    def __init__(self, key, locale=LOCALE, region="na", route="americas", reload=True):
        self.key = key
        self.route = route
        self.region = region
        self.fetch = requests.get

        if locale not in LOCALES:
            raise ValueError(
                f"The given locale '{locale}' is invalid. See "
                + "`valorant.values.LOCALES` for a list of valid locales."
            )
        else:
            self.locale = locale

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

        url = self.build_url(code=self.region, endpoint="content")
        heads = self.build_header({"X-Riot-Token": self.key})
        params = {"locale": self.locale}

        r = self.fetch(url, params=params, headers=heads)
        r.raise_for_status()

        self.set_attributes(r.json())

        return

    def build_header(self, mixin: dict, base: str = "web") -> dict:
        """Create a header dictionary from the default request headers."""

        c = HEADERS[base].copy()

        for n, v in mixin.items():
            c[n] = v

        return c

    def build_url(self, code: str = "na", endpoint: str = "content", base: str = "web") -> str:
        """Create a request URL with the given code and endpoint."""

        if code not in REGIONS and code not in ROUTES:
            raise ValueError(f"Invalid Route Code: '{code}'")
        else:
            url = WEB_API if base == "web" else CLIENT_API
            end = ENDPOINTS[base][endpoint]
            url = url.format(code=code) + end

            return url

    def get_user_by_puuid(self, puuid: str) -> AccountDTO:
        """Get a Riot account by the given puuid."""

        heads = self.build_header({"X-Riot-Token": self.key})

        url = self.build_url(code=self.route, endpoint="puuid")
        url = url.format(puuid=puuid)

        r = self.fetch(url, headers=heads)
        r.raise_for_status()

        return AccountDTO(r.json())

    def get_user_by_name(self, name: str, delim: str = "#") -> AccountDTO:
        """Get a Riot account by a given name split by a delimiter."""
        heads = self.build_header({"X-Riot-Token": self.key})
        values = name.split(delim)
        values = [urllib.parse.quote(v, safe=SAFES) for v in values]

        url = self.build_url(code=self.route, endpoint="game-name")
        url = url.format(name=values[0], tag=values[1])

        r = self.fetch(url, headers=heads)
        r.raise_for_status()

        return AccountDTO(r.json())

    def get_platform_status(self) -> PlatformDataDTO:
        """Get the current platform status for Valorant."""
        url = self.build_url(code=self.region, endpoint="status")
        heads = self.build_header({"X-Riot-Token": self.key})
        params = {"locale": self.locale}

        r = self.fetch(url, headers=heads, params=params)
        r.raise_for_status()

        return PlatformDataDTO(r.json())

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

        url = self.build_url(self.region, endpoint="leaderboard")
        url = url.format(actID=actID)

        heads = self.build_header({"X-Riot-Token": self.key})
        params = {"locale": self.locale, "size": size, "startIndex": size * page}

        r = self.fetch(url, headers=heads, params=params)
        r.raise_for_status()

        return LeaderboardDTO(r.json())

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
