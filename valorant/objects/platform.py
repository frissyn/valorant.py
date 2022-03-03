import typing as t

from .content import ContentList
from .dto import DTO


class PlatformContentDTO(DTO):
    locale: str
    content: str


class UpdateDTO(DTO):
    id: str
    author: str
    publish: bool
    publish_locations: t.Iterable[str]
    translations: t.Iterable[PlatformContentDTO]
    created_at: str
    updated_at: str

    def __init__(self, obj):
        super().__init__(obj)

        self.translations = ContentList(
            PlatformContentDTO(t) for t in obj["translations"]
        )


class StatusDTO(DTO):
    id: str
    maintenance_status: str
    incident_severity: str
    titles: t.Iterable[PlatformContentDTO]
    updates: t.Iterable[UpdateDTO]
    created_at: str
    archive_at: str
    updated_at: str
    platforms: t.Iterable[str]

    def __init__(self, obj):
        super().__init__(obj)

        self.titles = ContentList(PlatformContentDTO(t) for t in obj["titles"])
        self.updates = ContentList(UpdateDTO(u) for u in obj["updates"])


class PlatformDataDTO(DTO):
    name: str
    localizedNames: t.Mapping[str, str]
    id: str
    locales: str
    maintenances: t.Iterable[StatusDTO]
    incidents: t.Iterable[StatusDTO]

    def __init__(self, obj):
        super().__init__(obj)

        self.maintenances = ContentList(StatusDTO(m) for m in obj["maintenances"])
        self.incidents = ContentList(StatusDTO(i) for i in obj["incidents"])
