import os
import json
import base64
import requests

from .values import REGIONS

class LocalClient(object):
    def __init__(self, reigon="na"):
        self.reigon = reigon if reigon in REGIONS else "na"
        self.lockfile = "".join(
            os.getenv('LOCALAPPDATA'),
            "Riot Games\\Riot Client\\Config\\lockfile"
        )
        
        with open(self.lockfile, "r") as f:
            data = f.read().split(":")
        
        self.auth = base64.encode(f"riot:{data[3]}")
        self.base_url = f"https://127.0.0.1:{data[2]}/"

        self.s = requests.Session()
        self.s.headers.update({
            "Authorization": f"Basic {self.auth}"
        })

    def _url(self, path: str):
        return self.base_url + path

    def get_session(self):
        data = self.s.get(self._url("/chat/v1/session"))

        return json.loads(data.content)["data"]
