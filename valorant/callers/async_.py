import aiohttp
import typing as t

from .base import BaseCaller


class AsyncCaller(BaseCaller):
    def __init__(self, key: t.Text, **options):
        self.params = {"locale": options.get("locale")}

        super().__init__(key, aiohttp.ClientSession, async_=True, **options)

    async def call(
        self,
        method: t.Text,
        endpoint: t.Text,
        escapes: t.Tuple[int, ...] = (),
        params: t.Mapping = {},
        route: t.Optional[t.Text] = False,
        **extras,
    ) -> t.Optional[t.Mapping[str, t.Any]]:
        url = self.build_url(endpoint, route, **extras)
        r = await self.session.request(method, url, params=self.params.update(params))

        if r.status in escapes:
            return None

        return r.raise_for_status() or (await r.json())
