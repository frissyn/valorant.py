import json
import typing as t

from .content import ContentList
from .dto import DTO

from ..caller import WebCaller


class LeaderboardPlayerDTO(DTO):
    puuid: str
    gameName: str
    tagLine: str
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int


class LeaderboardDTO(DTO):
    shard: str
    actId: str
    totalPlayers: int
    players: t.List[LeaderboardPlayerDTO]

    def __init__(self, obj):
        super().__init__(obj)

        self.players = ContentList(LeaderboardPlayerDTO(p) for p in obj["players"])


class LeaderboardIterator:
    def __init__(self, caller: WebCaller, pages: int = 1, **params):
        self.handle = caller
        self.kwargs = params
        self.index, self.pages = 0, pages

    def __iter__(self):
        return self

    def __next__(self) -> LeaderboardDTO:
        if self.index >= self.pages:
            raise StopIteration
        else:
            self.index += 1

            payload = {
                "actID": self.kwargs["actID"],
                "params": {
                    "size": self.kwargs["size"],
                    "startIndex": (self.index - 1) * self.kwargs["size"],
                },
            }

            data = self.handle.call("GET", "leaderboard", **payload)

            return LeaderboardDTO(data)
