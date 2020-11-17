import locale
import requests

from .dto import ActDTO
from .dto import AccountDTO
from .dto import ContentItemDTO
from .dto import PlatformDataDTO

from .errors import APIError
from .errors import InvalidKeyError

LOCALE = locale.getlocale()[0].replace("_", "-")
CONTENT_URL = "https://na.api.riotgames.com/val/content/v1/contents"
STATUS_URL = "https://na.api.riotgames.com/val/status/v1/platform-data"
ACCOUNT_URL = (
    "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{0}/{1}"
)
headerMixin = {"Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"}


def update_dict(stale, latest):
    for key, items in latest.items():
        stale[key] = latest[key]

    return stale


class Client(object):
    def __init__(self, key, locale=LOCALE):
        if not self.verify_key(key):
            raise InvalidKeyError(
                f"Your provided API Key: {key} is invalid or expired."
            )
        else:
            self.key = key
            self.locale = locale
            self.reload()

    def __getattribute__(self, name):
        return super(Client, self).__getattribute__(name)

    def set_attributes(self, attrs):
        for attr, value in attrs.items():
            self.__setattr__(attr, value)

    def reload(self):
        headers = update_dict(headerMixin, {"X-Riot-Token": self.key})
        params = {"locale": self.locale}
        r = requests.get(CONTENT_URL, params=params, headers=headers).json()

        self.set_attributes(r)

    def verify_key(self, key):
        headers = update_dict(headerMixin, {"X-Riot-Token": key})
        r = requests.get(CONTENT_URL, headers=headers)

        if str(r.status_code)[0] != "2":
            return False
        else:
            return True

    def get_user(self, fullname):
        name = fullname.split("#")[0]
        tag = fullname.split("#")[-1]

        headers = update_dict(headerMixin, {"X-Riot-Token": self.key})
        r = requests.get(ACCOUNT_URL.format(name, tag), headers=headers)

        if str(r.status_code)[0] == "2":
            return AccountDTO(r.json())
        else:
            raise APIError(r.text)

    def get_platform_status(self):
        headers = update_dict(headerMixin, {"X-Riot-Token": self.key})
        r = requests.get(STATUS_URL, headers=headers)

        if str(r.status_code)[0] == "2":
            return PlatformDataDTO(r.json())
        else:
            raise APIError(r.text)

    def get_acts(self):
        acts = []
        for a in self.acts:
            acts.append(ActDTO(a))
        return acts

    def get_characters(self):
        characters = []
        for c in self.characters:
            characters.append(ContentItemDTO(c))
        return characters

    def get_charms(self):
        charms = []
        for c in self.charms:
            charms.append(ContentItemDTO(c))
        return charms

    def get_charm_levels(self):
        charmLevels = []
        for c in self.charmLevels:
            charmLevels.append(ContentItemDTO(c))
        return charmLevels

    def get_chromas(self):
        chromas = []
        for c in self.chromas:
            chromas.append(ContentItemDTO(c))
        return chromas

    def get_equips(self):
        equips = []
        for e in self.equips:
            equips.append(ContentItemDTO(e))
        return equips

    def get_maps(self):
        maps = []
        for m in self.maps:
            maps.append(ContentItemDTO(m))
        return maps

    def get_skins(self):
        skins = []
        for s in self.skins:
            skins.append(ContentItemDTO(s))
        return skins

    def get_skin_levels(self):
        skinLevels = []
        for s in self.skinLevels:
            skinLevels.append(ContentItemDTO(s))
        return skinLevels

    def get_game_modes(self):
        gameModes = []
        for g in self.gameModes:
            gameModes.append(ContentItemDTO(g))
        return gameModes

    def get_sprays(self):
        sprays = []
        for s in self.sprays:
            sprays.append(ContentItemDTO(s))
        return sprays

    def get_spray_levels(self):
        sprayLevels = []
        for s in self.sprayLevels:
            sprayLevels.append(ContentItemDTO(s))
        return sprayLevels

    def get_player_cards(self):
        playerCards = []
        for p in self.playerCards:
            playerCards.append(ContentItemDTO(p))
        return playerCards

    def get_player_titles(self):
        playerTitles = []
        for p in self.playerTitles:
            playerTitles.append(ContentItemDTO(p))
        return playerTitles
