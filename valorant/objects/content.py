import typing as t

from .dto import DTO


class ActDTO(DTO):
    name: str
    localizedNames: t.Mapping[str, str]
    id: str
    isActive: bool

    def __getattribute__(self, name):
        return super(ActDTO, self).__getattribute__(name)


class ContentItemDTO(DTO):
    name: str
    localizedNames: t.Optional[t.Mapping[str, str]]
    id: str
    assetName: str
    assetPath: str

    def __init__(self, obj):
        super().__init__(obj)

        if obj["get"]("localizedNames"):
            self.localizedNames = obj["localizedNames"]
        else:
            self.localizedNames = None

    def __getattribute__(self, name):
        return super(ContentItemDTO, self).__getattribute__(name)


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

        self.acts = ContentList(obj["acts"])
        self.characters = ContentList(obj["characters"])
        self.maps = ContentList(obj["maps"])
        self.chromas = ContentList(obj["chromas"])
        self.skins = ContentList(obj["skins"])
        self.skinLevels = ContentList(obj["skinLevels"])
        self.equips = ContentList(obj["equips"])
        self.gameModes = ContentList(obj["gameModes"])
        self.sprays = ContentList(obj["sprays"])
        self.sprayLevels = ContentList(obj["sprayLevels"])
        self.charms = ContentList(obj["charms"])
        self.charmLevels = ContentList(obj["charmLevels"])
        self.playerCards = ContentList(obj["playerCards"])
        self.playerTitles = ContentList(obj["playerTitles"])


    def __getattribute__(self, name):
        return super(ContentDTO, self).__getattribute__(name)


class ContentList(list, object):
    def find(self, value: str, attr: str, default=None):
        """Find an item in the ContentList by it's given attribute value."""
        for item in self.copy():
            try:
                if getattr(item, attr) == value:
                    return item
                else:
                    continue
            except AttributeError:
                continue

        return default
