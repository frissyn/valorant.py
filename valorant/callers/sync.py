import requests
import typing as t

from .base import BaseCaller


class WebCaller(BaseCaller):
    def __init__(self, key, **options):
        self.params = {"locale": options.get("locale")}

        super().__init__(key, requests.Session, **options)

    def call(
        self,
        method: t.Text,
        endpoint: t.Text,
        escapes: t.Tuple[int, ...] = (),
        params: t.Mapping = {},
        route: t.Optional[t.Text] = False,
        **extras,
    ) -> t.Optional[t.Mapping[str, t.Any]]:
        url = self.build_url(endpoint, route, **extras)
        r = self.session.request(method, url, params=self.params.update(params))

        if r.status_code in escapes:
            return None

        return r.raise_for_status() or r.json()
