import json
import typing as t


class DTOEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, DTO):
            return o._json

        return json.JSONEncoder.default(self, o)


class DTO(object):
    _json: t.Mapping[str, t.Any]

    def __init__(self, obj: t.Mapping[str, t.Any]):
        self._json = obj
        self.set_attributes(obj)

    def __str__(self) -> t.Text:
        s = f"<class {self.__class__.__name__} "

        for a in dir(self):
            v = getattr(self, a)

            if not a.startswith("_") and not callable(v):
                s += f"@{a}={v} "

        return f"{s[:-1]}>"

    def __repr__(self) -> t.Text:
        return self.dumps()

    @classmethod
    def optional(cls, obj: t.Optional[t.Mapping]) -> t.Optional:
        if obj != None:
            return cls.__init__(obj)

        return None

    def json(self) -> t.Mapping:
        return self._json

    def dumps(self, **kw: t.Mapping) -> t.Text:
        return json.dumps(self._json, cls=DTOEncoder, **kw)

    def set_attributes(self, attrs: t.Mapping, sub: bool = False) -> t.Optional:
        for attr, value in attrs.items():
            if sub and isinstance(value, dict):
                self.__setattr__(attr, DTO(value))
            elif sub and isinstance(value, list):
                for i, item in enumerate(value):
                    value[i] = DTO(item)

                self.__setattr__(attr, value)
            else:
                self.__setattr__(attr, value)
