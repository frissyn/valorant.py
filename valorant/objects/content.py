import re
import typing as t
import operator as op

from .dto import DTO
from ..query import Expression


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
    acts: t.List[ActDTO]
    characters: t.List[ContentItemDTO]
    maps: t.List[ContentItemDTO]
    chromas: t.List[ContentItemDTO]
    skins: t.List[ContentItemDTO]
    skinLevels: t.List[ContentItemDTO]
    equips: t.List[ContentItemDTO]
    gameModes: t.List[ContentItemDTO]
    sprays: t.List[ContentItemDTO]
    sprayLevels: t.List[ContentItemDTO]
    charms: t.List[ContentItemDTO]
    charmLevels: t.List[ContentItemDTO]
    playerCards: t.List[ContentItemDTO]
    playerTitles: t.List[ContentItemDTO]

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


def _fmt(key: t.Text) -> t.Text:
    if key.startswith("__") and key.endswith("__"):
        return re.sub(r"_{6}", "__.__", key)
    else:
        return re.sub(r"__(?!_)", ".", key)


def _operate(a, b):
    if isinstance(b, Expression):
        return b.statement(a)
    elif callable(b):
        return b(a)
    else:
        return op.eq(a, b)


class ContentList(list):
    def __init__(self, loop: t.List[t.Any]):
        super(ContentList, self).__init__(loop)

    def get(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        if value != None:
            attrs = {"name": value}

        funcs = [(attr(_fmt(key)), v) for key, v in attrs.items()]

        for el in self:
            if all(_operate(func(el), value) for func, value in funcs):
                return el

        return None

    def find(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        return self.get(value=value, **attrs)

    def get_all(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        results = []

        if value != None:
            attrs = {"name": value}

        funcs = [(attr(_fmt(key)), v) for key, v in attrs.items()]

        for el in self:
            if all(_operate(func(el), value) for func, value in funcs):
                results.append(el)

        return results

    def find_all(
        self, value: t.Optional[T] = None, **attrs: t.Mapping[t.Text, T]
    ) -> t.Optional[T]:
        return self.get_all(value=value, **attrs)
