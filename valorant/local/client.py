import os
import ssl
import json
import requests

from ..lexicon import Lex


class LocalClient(object):
    """Client for interacting with the local instance of the VALORANT application.
    This is called the `RCS API`. The game must be running for this class to function
    properly. Currently unstable, complete support is coming soon.

    .. warning::
        While interacting with the RCS API is not
        `explicitly disallowed <https://reddit.com/r/VALORANT/comments/oae5g6/comment/h3hwxtf>`_,
        please have some common sense. ``valorant.py`` is not liable for any punishment
        you may recieve if you break Riot's Terms of Service. (`i.e. creating an Auto
        Agent Selector`)

    :param region:
        The region to instance the client with. If this doesn't match the game's
        region there could be some unexpected behavior.
    :type region: str
    """

    def __init__(self, reigon="na"):
        if reigon not in Lex.REGIONS:
            raise ValueError(f"'{reigon}' is not a supported reigon for LocalClient.")

        self.reigon = reigon
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
        """Get the current session of the player at the moment this function
        is  called. Represents data for being in-queue, in-match, idle, etc.

        :rtype: dict
        """
        data = self.s.get(self._url("/chat/v1/session"), verify=ssl.CERT_NONE)

        return json.loads(data.content)

    def get_presences(self, user=False) -> dict:
        """Get presence data for everyone connected to the player's lobby. If the
        player is in a match, this will return session data for all players in a
        match. Same goes for queue, party, etc.

        :param user: If ``True``, only returns presence data for the current player.
        :type user: bool

        :rtype: dict
        """
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
