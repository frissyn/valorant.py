import valorant

from tests import BaseTest


class TestRanked(BaseTest):
    def setUp(self):
        super().setUp()

        self.lb = self.client.get_leaderboard(10)
        self.iterator = self.client.get_leaderboard(pages=3, size=10)

    def test_leaderboard_attributes(self):
        for name in [
            "actId",
            "players",
            "totalPlayers",
            "startIndex",
            "query",
            "shard",
        ]:
            self.assertHasAttr(self.lb, name)

    def test_leaderboard_players(self):
        lb = self.client.get_leaderboard(10)

        for player in lb.players:
            for name in [
                "gameName",
                "leaderboardRank",
                "numberOfWins",
                "puuid",
                "rankedRating",
                "tagLine",
            ]:
                self.assertHasAttr(player, name)

    def test_leaderboard_iteration(self):
        for i in range(self.iterator.pages):
            next(self.iterator)

        with self.assertRaises(StopIteration):
            next(self.iterator)
