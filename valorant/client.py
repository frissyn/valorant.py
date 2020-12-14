import locale
import requests

from .dto import ActDTO
from .dto import AccountDTO
from .dto import ContentItemDTO
from .dto import PlatformDataDTO

LOCALE = locale.getlocale()[0].replace("_", "-")
CONTENT_URL = "https://na.api.riotgames.com/val/content/v1/contents"
STATUS_URL = "https://na.api.riotgames.com/val/status/v1/platform-data"
PUUID_URL = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-puuid/{puuid}"
GAMENAME_URL = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}"
headerMixin = {"Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8"}


def update_dict(stale, latest):
    for key, items in latest.items():
        stale[key] = latest[key]

    return stale


class Client(object):
    def __init__(self, key, locale=LOCALE):
        self.key = key
        self.locale = locale
        self.fetch = requests.get
        self.reload()

    def __getattribute__(self, name):
        return super(Client, self).__getattribute__(name)

    def set_attributes(self, attrs):
        for attr, value in attrs.items():
            self.__setattr__(attr, value)

    def reload(self):
        headers = update_dict(headerMixin, {"X-Riot-Token": self.key})
        params = {"locale": self.locale}
        r = self.fetch(CONTENT_URL, params=params, headers=headers)
        r.raise_for_status()

        self.set_attributes(r.json())

    def get_user(self, value, via="puuid"):
        headers = update_dict(headerMixin, {"X-Riot-Token": self.key})

        if via == "puuid":
            target = PUUID_URL.format(puuid=value)
        elif via == "name":
            name = value.split("#")[0]
            tag = value.split("#")[-1]

            target = GAMENAME_URL.format(name=name, tag=tag)

            r = self.fetch(target, headers=headers)

        r.raise_for_status()

        return AccountDTO(r.json())

    def get_platform_status(self):
        headers = update_dict(headerMixin, {"X-Riot-Token": self.key})
        r = self.fetch(STATUS_URL, headers=headers)
        r.raise_for_status()

        return PlatformDataDTO(r.json())

    def get_acts(self):
        acts = [ActDTO(a) for a in self.acts]

        return acts

    def get_characters(self):
        characters = [ContentItemDTO(c) for c in self.characters]

        return characters

    def get_charms(self):
        charms = [ContentItemDTO(c) for c in self.charms]

        return charms

    def get_charm_levels(self):
        charmLevels = [ContentItemDTO(c) for c in self.charmLevels]

        return charmLevels

    def get_chromas(self):
        chromas = [ContentItemDTO(c) for c in self.chromas]

        return chromas

    def get_equips(self):
        equips = [ContentItemDTO(e) for e in self.equips]

        return equips

    def get_maps(self):
        maps = [ContentItemDTO(m) for m in self.maps]

        return maps

    def get_skins(self):
        skins = [ContentItemDTO(s) for s in self.skins]

        return skins

    def get_skin_levels(self):
        skinLevels = [ContentItemDTO(s) for s in self.skinLevels]

        return skinLevels

    def get_game_modes(self):
        gameModes = [ContentItemDTO(g) for g in self.gameModes]

        return gameModes

    def get_sprays(self):
        sprays = [ContentItemDTO(s) for s in self.sprays]

        return sprays

    def get_spray_levels(self):
        sprayLevels = [ContentItemDTO(s) for s in self.sprayLevels]

        return sprayLevels

    def get_player_cards(self):
        playerCards = [ContentItemDTO(p) for p in self.playerCards]

        return playerCards

    def get_player_titles(self):
        playerTitles = [ContentItemDTO(p) for p in self.playerTitles]

        return playerTitles

