import typing as t

from .dto import DTO


class PlatformContentDTO(DTO):
    locale: str
    content: str


class UpdateDTO(DTO):
    id: str
    author: str
    publish: bool
    publish_locations: t.List[str]
    translations: t.List[PlatformContentDTO]
    created_at: str
    updated_at: str

    def __init__(self, obj):
        super().__init__(obj)

        self.translations = [PlatformContentDTO(t) for t in obj["translations"]]


class StatusDTO(DTO):
    id: str
    maintenance_status: str
    incident_severity: str
    titles: t.List[PlatformContentDTO]
    updates: t.List[UpdateDTO]
    created_at: str
    archive_at: str
    updated_at: str
    platforms: t.List[str]

    def __init__(self, obj):
        super().__init__(obj)

        self.titles = [PlatformContentDTO(t) for t in obj["titles"]]
        self.updates = [UpdateDTO(u) for u in obj["updates"]]


class PlatformDataDTO(DTO):
    name: str
    localizedNames: t.Mapping[str, str]
    id: str
    locales: str
    maintenances: t.List[StatusDTO]
    incidents: t.List[StatusDTO]

    def __init__(self, obj):
        super().__init__(obj)

        self.maintenances = [StatusDTO(m) for m in obj["maintenances"]]
        self.incidents = [StatusDTO(i) for i in obj["incidents"]]
