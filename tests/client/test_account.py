import valorant

from tests import BaseTest


class TestAccount(BaseTest):
    def test_account(self):
        acc = self.client.get_user(
            "B-"
            "_urbbPjxhSekDzdIS7fznZ6w82fss8PBd1OnOIiJ"
            "_7wNdRyj4cljexSBoGCESzJglohUbAM4H5kw"
        )

        self.assertIsInstance(acc, valorant.AccountDTO)
        self.assertEqual(getattr(acc, "gameName", None), "frissyn")

    def test_account_by_name(self):
        # Using my static alternate account.
        acc = self.client.get_user_by_name("friss#sick")

        self.assertIsInstance(acc, valorant.AccountDTO)
        self.assertEqual(getattr(acc, "gameName", None), "friss")
