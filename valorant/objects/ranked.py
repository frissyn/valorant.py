import typing as t

from .content import ContentList
from .dto import DTO


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

        # self.players = ContentList()

        # for p in obj["players"]:
        #     if obj.get("gameName"):
        #         self.players.append(LeaderboardPlayerDTO(p))
