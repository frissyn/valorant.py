class DTO(object):
    """Base mixin class for synthesizing JSON responses from the API."""

    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

    def __str__(self):
        return str(self.json)

    def __repr__(self):
        return str(self.json)

    def set_attributes(self, attrs, sub=False):
        for attr, value in attrs.items():
            if sub and isinstance(value, dict):
                self.__setattr__(attr, DTO(value))
            elif sub and isinstance(value, list):
                for i, item in enumerate(value):
                    value[i] = DTO(item)

                self.__setattr__(attr, value)
            else:
                self.__setattr__(attr, value)


class AccountDTO(DTO):
    def __init__(self, obj, handle):
        self.json = obj
        self.handle = handle
        self.set_attributes(obj)

    def matchlist(self):
        l = self.handle.call("GET", "matchlists", puuid=self.puuid)

        return MatchlistDTO(l, self.handle)


class ActDTO(DTO):
    def __getattribute__(self, name):
        return super(ActDTO, self).__getattribute__(name)


class ContentItemDTO(DTO):
    def __getattribute__(self, name):
        return super(ContentItemDTO, self).__getattribute__(name)


class PlatformDataDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj, sub=True)

    def __getattribute__(self, name):
        return super(PlatformDataDTO, self).__getattribute__(name)


class PlayerDTO(DTO):
    def __getattribute__(self, name):
        return super(PlayerDTO, self).__getattribute__(name)


class LeaderboardDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj)

        plys = [PlayerDTO(p) for p in obj["players"]]
        self.players = ContentList(plys)

    def __getattribute__(self, name):
        return super(LeaderboardDTO, self).__getattribute__(name)


class MatchDTO(DTO):
    def __init__(self, obj):
        self.json = obj
        self.set_attributes(obj, sub=True)


class MatchlistEntryDTO(DTO):
    def __init__(self, obj, handle):
        self.json = obj
        self.handle = handle
        self.set_attributes(obj)

    def get(self):
        match = self.handle.call("GET", "match", matchID=self.id)

        return MatchDTO(match)


class MatchlistDTO(DTO, list):
    def __init__(self, obj, handle):
        self.json = obj
        self.set_attributes(obj)

        for i, e in enumerate(self.history):
            self.history[i] = MatchlistEntryDTO(e, handle)
            self.history[i].id = e["matchId"]

    def __getattribute__(self, name):
        return super(MatchlistDTO, self).__getattribute__(name)


class ContentList(list, object):
    def get(self, name: str, default=None):
        """Safe method for getting items in the ContentList by name attr."""
        for item in self.copy():
            try:
                if item.name == name:
                    return item
                else:
                    continue
            except AttributeError:
                continue

        return default

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
