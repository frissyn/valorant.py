import typing as t

from .dto import DTO


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

        if obj.get("localizedNames"):
            self.localizedNames = obj["localizedNames"]
        else:
            self.localizedNames = None


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

        self.acts = ContentList([ActDTO(i) for i in obj["acts"]])
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
        self.playerTitles = ContentList(
            [ContentItemDTO(i) for i in obj["playerTitles"]]
        )


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
