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
