import typing as t

from .content import ContentList
from .dto import DTO

from ..caller import WebCaller


class LeaderboardPlayerDTO(DTO):
    puuid: t.Optional[str]
    gameName: t.Optional[str]
    tagLine: t.Optional[str]
    leaderboardRank: int
    rankedRating: int
    numberOfWins: int

    def __init__(self, obj):
        super().__init__(obj)

        for name in ["gameName", "tagLine", "puuid"]:
            if not obj.get(name):
                self.__setattr__(name, None)


class LeaderboardDTO(DTO):
    shard: str
    actId: str
    totalPlayers: int
    players: t.List[LeaderboardPlayerDTO]

    def __init__(self, obj):
        super().__init__(obj)

        self.players = ContentList(LeaderboardPlayerDTO(p) for p in obj["players"])


class LeaderboardIterator:
    """Simple iterator utility for getting multiple leaderboard pages.
    Each iteraction returns a :class:`LeaderboardDTO`. See
    :func:`Client.get_leaderboard` for more info.
    """

    def __init__(self, caller: WebCaller, pages: int = 1, **params):
        self._handle = caller
        self.kwargs = params
        self.index, self.pages = 0, pages

    def __iter__(self):
        return self

    def __next__(self) -> LeaderboardDTO:
        if self.index >= self.pages:
            raise StopIteration

        payload = {
            "actID": self.kwargs["actID"],
            "params": {
                "size": self.kwargs["size"],
                "startIndex": (self.index) * self.kwargs["size"],
            },
        }

        self.index += 1
        data = self._handle.call("GET", "leaderboard", **payload)

        return LeaderboardDTO(data)
