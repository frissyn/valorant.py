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

        if obj.get("localizedNames"):
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

        self.acts = ContentList([ContentItemDTO(i) for i in obj["acts"]])
        self.characters = ContentList([ContentItemDTO(i) for i in obj["characters"]])
        self.maps = ContentList([ContentItemDTO(i) for i in obj["maps"]])
        self.chromas = ContentList([ContentItemDTO(i) for i in obj["chromas"]])
        self.skins = ContentList([ContentItemDTO(i) for i in obj["skins"]])
        self.skinLevels = ContentList([ContentItemDTO(i) for i in obj["skinLevels"]])
        self.equips = ContentList([ContentItemDTO(i) for i in obj["equips"]])
        self.gameModes = ContentList([ContentItemDTO(i) for i in obj["gameModes"]])
        self.sprays = ContentList([ContentItemDTO(i) for i in obj["sprays"]])
        self.sprayLevels = ContentList([ContentItemDTO(i) for i in obj["sprayLevels"]])
        self.charms = ContentList([ContentItemDTO(i) for i in obj["charms"]])
        self.charmLevels = ContentList([ContentItemDTO(i) for i in obj["charmLevels"]])
        self.playerCards = ContentList([ContentItemDTO(i) for i in obj["playerCards"]])
        self.playerTitles = ContentList([ContentItemDTO(i) for i in obj["playerTitles"]])

    def __getattribute__(self, name):
        return super(ContentDTO, self).__getattribute__(name)


class ContentList(list):
    def find(self, **attributes: t.Mapping) -> t.Optional[DTO]:
        checks = 0

        for item in self:
            for attr, value in attributes.items():
                if attr == "assetName":
                    genexpr = lambda m: value.endswith(getattr(item, attr))
                else:
                    genexpr = lambda m: getattr(item, attr) == value

                try: 
                    if genexpr(item): 
                        checks += 1
                except AttributeError: 
                    pass

            if checks == len(attributes):
                return item
            else:
                checks = 0 