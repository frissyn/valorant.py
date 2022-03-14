import valorant

from tests import BaseTest


class TestAccount(BaseTest):
    def test_account(self):
        acc = self.client.get_user(
            "B-"
            "_urbbPjxhSekDzdIS7fznZ6w82fss8PBd1OnOIiJ"
            "_7wNdRyj4cljexSBoGCESzJglohUbAM4H5kw"
        )

        self.assertEqual(getattr(acc, "gameName", None), "frissyn")
        self.assertIsInstance(acc, valorant.AccountDTO)

    def test_account_by_name(self):
        acc = self.client.get_user_by_name("frissyn#6969")

        self.assertEqual(getattr(acc, "gameName", None), "frissyn")
        self.assertIsInstance(acc, valorant.AccountDTO)
