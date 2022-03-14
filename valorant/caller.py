import requests
import typing as t

from .lexicon import Lex


def value_check(*args: t.List[t.Text]) -> bool:
    KEYS = Lex.ROUTES + Lex.LOCALES + Lex.REGIONS

    for arg in args:
        if arg not in KEYS:
            raise ValueError(
                f"`{arg}` is either an unspported or invalid geographical value."
            )
        else:
            return True

    return False


class WebCaller(object):
    def __init__(self, token: t.Text, locale: t.Text, region: t.Text, route: t.Text):
        self.base = "https://{root}.api.riotgames.com/"
        self.eps = Lex.ENDPOINTS["web"]
        self.sess = requests.Session()
        self.sess.params.update({"locale": locale})
        self.sess.headers.update(
            {
                "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
                "User-Agent": "Mozilla/5.0",
                "X-Riot-Token": token,
            }
        )

        if value_check(region, route):
            self.locale = locale
            self.region = region
            self.route = route

    def call(
        self,
        m: t.Text,
        ep: t.Text,
        params: t.Optional[t.Mapping] = None,
        route: t.Optional[t.Text] = False,
        **kw,
    ) -> t.Mapping[str, t.Any]:
        prefix = self.base.format(root=self.route if route else self.region)
        url = prefix + self.eps[ep].format(**kw)

        r = self.sess.request(m, url, params=params)
        r.raise_for_status()

        return r.json()
