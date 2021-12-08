import typing as t

from .dto import DTO


class PlatformContentDTO(DTO):
    locale: str
    content: str

    def __getattribute__(self, name):
        return super(PlatformContentDTO, self).__getattribute__(name)


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

        self.translations = [PlatformContentDTO(t) for t in obj["translations"]]

    def __getattribute__(self, name):
        return super(UpdateDTO, self).__getattribute__(name)


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

        self.titles = [PlatformContentDTO(t) for t in obj["titles"]]
        self.updates = [UpdateDTO(u) for u in obj["updates"]]

    def __getattribute__(self, name):
        return super(StatusDTO, self).__getattribute__(name)


class PlatformDataDTO(DTO):
    name: str
    localizedNames: t.Mapping[str, str]
    id: str
    locales: str
    maintenances: t.Iterable[StatusDTO]
    incidents: t.Iterable[StatusDTO]

    def __init__(self, obj):
        super().__init__(obj)

    def __getattribute__(self, name):
        return super(PlatformDataDTO, self).__getattribute__(name)
