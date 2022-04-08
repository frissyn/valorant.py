import typing as t

from ..lexicon import Lex


class BaseCaller(object):
    headers: t.Mapping[str, str] = {
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0",
        "X-Riot-Token": None,
    }

    def __init__(
        self,
        key: t.Text,
        ctx: t.Any,
        headers: t.Mapping = {},
        async_: bool = False,
        **options: t.Mapping,
    ):
        self.token = key
        self.async_ = async_
        self.endpoints = Lex.ENDPOINTS["web"].copy()
        self.base = "https://{code}.api.riotgames.com/"
        self.headers["X-Riot-Token"] = key

        try:
            self.session = ctx(headers=self.headers)
        except TypeError:
            self.session = ctx()
            self.session.headers = self.headers

        valids = Lex.ROUTES + Lex.LOCALES + Lex.REGIONS

        for name, value in options.items():
            if value not in valids and not (value is None and name == 'locale'):
                raise ValueError(f"'{value}' is not a valid {name}.")

            self.__setattr__(name, value)

    def build_url(self, endpoint: t.Text, route: t.Text, **extras) -> t.Text:
        url = self.base.format(code=route if route else self.region)

        return url + self.endpoints[endpoint].format(**extras)
