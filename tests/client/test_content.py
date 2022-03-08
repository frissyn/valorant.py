import valorant

from tests import BaseTest


class TestContent(BaseTest):
    def test_content(self):
        content = self.client.get_content(cache=True)

        self.assertIsInstance(content, valorant.ContentDTO)
        self.assertEqual(content, self.client.content)

    def test_asset(self):
        assets = {
            "gamemode": self.client.asset(assetName="BombGameMode"),
            "agent": self.client.asset(name="Viper"),
            "map": self.client.asset(id="7EAECC1B-4337-BBF6-6AB9-04B8F06B3319"),
        }

        self.assertEqual(assets["gamemode"].name, "Standard")
        self.assertEqual(assets["agent"].name, "Viper")
        self.assertEqual(assets["map"].name, "Ascent")

    def test_leaderboard(self):
        lb = self.client.get_leaderboard(100)

        self.assertIsInstance(lb, valorant.LeaderboardDTO)
