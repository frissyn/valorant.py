import os
import ssl
import json
import base64
import requests

from requests.sessions import Session

from .values import REGIONS


class LocalClient(object):
    def __init__(self, reigon="na"):
        self.reigon = reigon if reigon in REGIONS else "na"
        self.lockfile = "".join(
            [os.getenv("LOCALAPPDATA"), r"\Riot Games\Riot Client\Config\lockfile"]
        )

        with open(self.lockfile, "r") as f:
            data = f.read().split(":")

        self.base_url = f"{data[4]}://127.0.0.1:{data[2]}"

        self.s = requests.Session()
        self.s.auth = ("riot", data[3])

    def _url(self, path: str) -> str:
        return self.base_url + path

    def get_session(self) -> dict:
        data = self.s.get(self._url("/chat/v1/session"), verify=ssl.CERT_NONE)

        return json.loads(data.content)

    def get_presences(self, user=False) -> dict:
        data = self.s.get(self._url("/chat/v4/presences"), verify=ssl.CERT_NONE)
        data = json.loads(data.content)

        if user:
            puuid = self.get_session()["puuid"]

            for u in data["presences"]:
                if u["puuid"] == puuid:
                    return u
                else:
                    pass

            return {}
        else:
            return data
