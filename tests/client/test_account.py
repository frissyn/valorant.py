import valorant

from tests import BaseTest


class TestAccount(BaseTest):
    def test_account(self):
        acc = self.client.get_user(
            "B-_urbbPjxhSekDzdIS7fznZ6w82fss8PBd1OnOIiJ_7wNdRyj4cljexSBoGCESzJglohUbAM4H5kw"
        )

        self.assertEqual(acc.gameName, "frissyn")
        self.assertIsInstance(acc, valorant.AccountDTO)

    def test_account_by_name(self):
        acc = self.client.get_user_by_name("frissyn#6969")

        self.assertEqual(acc.gameName, "frissyn")
        self.assertIsInstance(acc, valorant.AccountDTO)

    def test_account_missing(self):
        acc = self.client.get_user(".")

        self.assertIsNone(acc)

    def test_account_missing_by_name(self):
        acc = self.client.get_user_by_name("missing#0000")

        self.assertIsNone(acc)