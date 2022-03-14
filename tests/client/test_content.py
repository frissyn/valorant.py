import valorant

from tests import BaseTest


class TestContent(BaseTest):
    def setUp(self):
        super().setUp()

        self.content = self.client.get_content(cache=True)

    def test_asset_1(self):
        asset = self.client.asset(name="Neon")

        self.assertEqual(asset.name, "Neon")

    def test_asset_2(self):
        asset = self.client.asset(id="7EAECC1B-4337-BBF6-6AB9-04B8F06B3319")

        self.assertEqual(asset.name, "Ascent")

    def test_content_attributes(self):
        for name in valorant.Lex.CONTENT_NAMES:
            self.assertHasAttr(self.content, name)
