import json
import locale
import requests

from .item import Item

from .errors import APIError
from .errors import InvalidKeyError

LOCALE = locale.getlocale()[0].replace("_", "-")
CONTENT_URL = "https://na.api.riotgames.com/val/content/v1/contents"
headerMixin = { "Accept-Charset" : "application/x-www-form-urlencoded; charset=UTF-8"}


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
		headers = update_dict(headerMixin, { "X-Riot-Token" : self.key })
		params = { "locale" : self.locale }
		r = requests.get(CONTENT_URL, params=params, headers=headers).json()

		self.set_attributes(r)
	
	def verify_key(self, key):
		headers = update_dict(headerMixin, {"X-Riot-Token" : key})
		r = requests.get(CONTENT_URL, headers=headers).json()

		if str(r.status_code)[0] != "2": return False
		else: return True

	def get_characters(self):
		return Item(self.characters)

	def get_chromas(self):
		return Item(self.chromas)
	
	def get_maps(self):
		return Item(self.maps)

	def get_skins(self):
		return Item(self.skins)

	def get_skin_levels(self):
		return Item(self.skinLevels)

	def get_equips(self):
		return Item(self.equips)
	
	def get_game_modes(self):
		return Item(self.gameModes)
	
	def get_sprays(self):
		return Item(self.sprays)
	
	def get_spray_levels(self):
		return Item(self.sprayLevels)
	
	def get_charms(self):
		return Item(self.charms)

	def get_charm_levels(self):
		return Item(self.charmLevels)

	def get_player_cards(self):
		return Item(self.playerCards)

	def get_player_titles(self):
		return Item(self.playerTitles)

	def get_acts(self):
		return Item(self.acts)