import json
import locale
import requests

#from .errors import APIError
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
			headers = update_dict(headerMixin, {"X-Riot-Token" : self.key})
			r = requests.get(CONTENT_URL, headers=headers).json()

			self.set_attributes(r)

	def __getattribute__(self, name):
		return super(Client, self).__getattribute__(name)

	def set_attributes(self, attrs):
		for attr, value in attrs.items():
			self.__setattr__(attr, value)
	
	def verify_key(self, key):
		headers = update_dict(headerMixin, {"X-Riot-Token" : key})
		r = requests.get(CONTENT_URL, headers=headers)

		if str(r.status_code)[0] != "2": return False
		else: return True
	
