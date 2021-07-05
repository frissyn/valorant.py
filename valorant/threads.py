import asyncio
import requests

from .client import Client

from .objects import ActDTO
from .objects import AccountDTO

# from .objects import ContentItemDTO
# from .objects import LeaderboardDTO
from .objects import PlatformDataDTO

from .objects import ContentList

# from .values import SAFES
# from .values import ROUTES
from .values import LOCALE
from .values import LOCALES

# from .values import REGIONS
# from .values import HEADERS
# from .values import WEB_API
# from .values import ENDPOINTS
# from .values import CLIENT_API


run = asyncio.run


class AsyncClient(Client):
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
            run(self.reload())
        else:
            pass

    def __getattribute__(self, name):
        return super(AsyncClient, self).__getattribute__(name)

    async def reload(self) -> None:
        """Reload the current cached response for the VAL-CONTENT endpoints."""
        return super().reload()

    async def get_user_by_puuid(self, puuid: str) -> AccountDTO:
        """Get a Riot account by the given puuid."""
        return super().get_user_by_puuid()

    async def get_user_by_name(self, name: str, delim: str = "#") -> AccountDTO:
        """Get a Riot account by a given name split by a delimiter."""
        return super().get_user_by_name()

    async def get_platform_status(self) -> PlatformDataDTO:
        """Get the current platform status for Valorant."""
        return super().get_platform_status()

    async def get_acts(self) -> ContentList:
        """Get a ContentList of Acts from Valorant."""
        return super().get_acts()

    async def get_characters(self) -> ContentList:
        """Get a ContentList of Agents from Valorant."""
        return super().get_characters()

    async def get_current_act(self) -> ActDTO:
        """Get the current Act (indiscriminate of episode)."""
        return super().get_current_act()

    async def get_charms(self) -> ContentList:
        """Get a ContentList of Gun Buddies from Valorant."""
        return super().get_charms()

    async def get_charm_levels(self) -> ContentList:
        """Get a ContentList of Gun Buddy Levels from Valorant."""
        return super().get_charm_levels()

    async def get_chromas(self) -> ContentList:
        return super().get_chromas()

    async def get_equips(self) -> ContentList:
        return super().get_equips()

    async def get_leaderboard(self, size: int = 100, page: int = 0, actID: str = ""):
        """Get the top user's in your client's region during a given Act."""
        return super().get_leaderboard()

    async def get_maps(self) -> ContentList:
        """Get a ContentList of Maps from Valorant."""
        return super().get_maps()

    async def get_skins(self) -> ContentList:
        """Get a ContentList of Weapon Skins from Valorant."""
        return super().get_skins()

    async def get_skin_levels(self) -> ContentList:
        """Get a ContentList of Weapon Skin Levels from Valorant."""
        return super().get_skin_levels()

    async def get_game_modes(self) -> ContentList:
        """Get a ContentList of Game Modes from Valorant."""
        return super().get_game_modes()

    async def get_sprays(self) -> ContentList:
        """Get a ContentList of Sprays from Valorant."""
        return super().get_sprays()

    async def get_spray_levels(self) -> ContentList:
        """Get a ContentList of Spray Levels from Valorant."""
        return super().get_spray_levels()

    async def get_player_cards(self) -> ContentList:
        """Get a ContentList of Player Cards from Valorant."""
        return super().get_player_cards()

    async def get_player_titles(self) -> ContentList:
        """Get a ContentList of Player Titles from Valorant."""
        return super().get_player_titles()
