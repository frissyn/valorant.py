import re
import typing as t
import operator as op

from .dto import DTO


T = t.TypeVar("T")
attr = op.attrgetter


class ActDTO(DTO):
    name: str
    localizedNames: t.Mapping[str, str]
    id: str
    isActive: bool


class ContentItemDTO(DTO):
    name: str
    localizedNames: t.Optional[t.Mapping[str, str]]
    id: str
    assetName: str
    assetPath: str

    def __init__(self, obj):
        super().__init__(obj)

        self.localizedNames = obj.get("localizedNames")


class ContentDTO(DTO):
    version: str
    acts: t.Iterable[ActDTO]
    characters: t.Iterable[ContentItemDTO]
    maps: t.Iterable[ContentItemDTO]
    chromas: t.Iterable[ContentItemDTO]
    skins: t.Iterable[ContentItemDTO]
    skinLevels: t.Iterable[ContentItemDTO]
    equips: t.Iterable[ContentItemDTO]
    gameModes: t.Iterable[ContentItemDTO]
    sprays: t.Iterable[ContentItemDTO]
    sprayLevels: t.Iterable[ContentItemDTO]
    charms: t.Iterable[ContentItemDTO]
    charmLevels: t.Iterable[ContentItemDTO]
    playerCards: t.Iterable[ContentItemDTO]
    playerTitles: t.Iterable[ContentItemDTO]

    def __init__(self, obj):
        super().__init__(obj)

        self.acts = ContentList(ActDTO(i) for i in obj["acts"])
        self.characters = ContentList(ContentItemDTO(i) for i in obj["characters"])
        self.maps = ContentList(ContentItemDTO(i) for i in obj["maps"])
        self.chromas = ContentList(ContentItemDTO(i) for i in obj["chromas"])
        self.skins = ContentList(ContentItemDTO(i) for i in obj["skins"])
        self.skinLevels = ContentList(ContentItemDTO(i) for i in obj["skinLevels"])
        self.equips = ContentList(ContentItemDTO(i) for i in obj["equips"])
        self.gameModes = ContentList(ContentItemDTO(i) for i in obj["gameModes"])
        self.sprays = ContentList(ContentItemDTO(i) for i in obj["sprays"])
        self.sprayLevels = ContentList(ContentItemDTO(i) for i in obj["sprayLevels"])
        self.charms = ContentList(ContentItemDTO(i) for i in obj["charms"])
        self.charmLevels = ContentList(ContentItemDTO(i) for i in obj["charmLevels"])
        self.playerCards = ContentList(ContentItemDTO(i) for i in obj["playerCards"])
        self.playerTitles = ContentList(ContentItemDTO(i) for i in obj["playerTitles"])


class ContentList(list):
    def __init__(self, loop: t.Iterable[t.Any]):
        super(ContentList, self).__init__(loop)

    def _fmt(self, key: str) -> str:
        if key.startswith("__") and key.endswith("__"):
            return re.sub(r"_{6}", "__.__", key)
        else:
            return re.sub(r"__(?!_)", ".", key)

    def get(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        if value != None:
            func = attr(self._fmt("name"))

            for el in self:
                if func(el) == value:
                    return el

            return None

        funcs = [(attr(self._fmt(key)), v) for key, v in attrs.items()]

        for el in self:
            if all(func(el) == value for func, value in funcs):
                return el

        return None

    def find(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        return self.find(value=value, **attrs)
