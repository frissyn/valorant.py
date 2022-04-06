import valorant
from valorant.query import exp

from tests import BaseTest


class TextExpression(BaseTest):
    def setUp(self, *a, **kw):
        super().setUp(*a, **kw)

        self.content = self.client.get_content(cache=True)

    def test_get(self):
        agent = self.content.characters.get(name=lambda x: "joy" in x)

        self.assertEqual(agent.name, "Killjoy")

    def test_get_all(self):
        maps_from_lambda = self.content.maps.get(name=lambda x: x.startswith("A"))
        maps_from_expr = self.content.maps.get(name=exp('.startswith', "A"))

        self.assertEqual(maps_from_lambda, maps_from_expr)
