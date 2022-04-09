from __future__ import annotations

import typing as t


class Lockfile(t.NamedTuple):
    path: str
    client: str
    unknown: int | str
    port: int | str
    password: str
    protocol: str

    @classmethod
    def new(cls, path: str) -> Lockfile:
        with open(path, "r+") as fh:
            data = fh.read().split(":")

        return cls(path, *data)
