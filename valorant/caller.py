import requests

from .values import ROUTES
from .values import LOCALES
from .values import REGIONS
from .values import ENDPOINTS


def value_check(*args):
    KEYS = ROUTES + LOCALES + REGIONS

    for arg in args:
        if arg not in KEYS:
            raise ValueError
            return False
        else:
            return True


class WebCaller(object):
    def __init__(self, token: str, locale: str, region: str, route: str):
        self.base = "https://{code}.api.riotgames.com/"
        self.eps = ENDPOINTS["web"]
        self.sess = requests.Session()
        self.sess.headers.update({
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0",
            "X-Riot-Token": token
        })

        if value_check(locale, region, route):
            self.locale = locale
            self.region = region
            self.route = route

    def call(self, m: str, ep: str, **kw):
        if ep not in list(self.eps.keys()):
            raise ValueError
        else:
            pass

        r = self.sess.request(m, f"{self.base}{self.eps[ep]}", **kw)
        r.raise_for_status()

        return r.json()


class ClientCaller(object):
    def __init__(self, token: str):
        self.base = "https://pd.{code}.a.pvp.net/"
        self.token = token

        self.sess = requests.Session()
        self.sess.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-Riot-Entitlements-JWT": "riot_entitlement"
        })

    def call(self, m: str, ep: str, **kw):
        pass
