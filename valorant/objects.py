import json

from datetime import datetime

class DTOEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, DTO):
            return o._json

        return json.JSONEncoder.default(self, o)

class DTO(object):
    """Represents a base object from the API."""
    
    def __init__(self, obj):
        self._json = obj
        self.set_attributes(obj)

    def __str__(self):
        return f"<class '{self.__class__.__name__}'>"

    def __repr__(self):
        s = f"<class {self.__class__.__name__} "

        for a in dir(self):
            v = getattr(self, a)
            
            if not a.startswith("_") and not callable(v):
                s += f"@{a}={v} "
        
        return f"{s}>"
    
    def json(self):
        return self._json
    
    def dumps(self, **kw):
        return json.dumps(self._json, cls=DTOEncoder, **kw)

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
        self._json = obj
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
        self._json = obj
        self.set_attributes(obj, sub=True)

    def __getattribute__(self, name):
        return super(PlatformDataDTO, self).__getattribute__(name)


class PlayerDTO(DTO):
    def __getattribute__(self, name):
        return super(PlayerDTO, self).__getattribute__(name)


class PlayerStatsDTO(DTO):
    def __init__(self, obj):
        super().__init__(obj)

        try: self.kd = self.kills / self.deaths
        except ZeroDivisionError: self.kd = self.kills

        try: self.kda = (self.kills + self.assists) / self.deaths
        except ZeroDivisionError: self.kda = self.kills + self.assists

        self.averageScore = self.score / self.roundsPlayed

    def __getattribute__(self, name):
        return super(PlayerStatsDTO, self).__getattribute__(name)


class LeaderboardDTO(DTO):
    def __init__(self, obj):
        super().__init__(obj)
        self.players = ContentList([PlayerDTO(p) for p in obj["players"]])

    def __getattribute__(self, name):
        return super(LeaderboardDTO, self).__getattribute__(name)


class MatchDTO(DTO):
    def __init__(self, obj):
        self._json = obj
        self.id = obj["matchInfo"]["matchId"]
        self.set_attributes(obj, sub=True)

        for p in self.players:
            try:
                p.__setattr__("stats", PlayerStatsDTO(p.stats))
            except AttributeError:
                pass
    
    def get_team(self, name):
        return next((t for t in self.teams if t.teamId == name), None)
    
    def get_timestamp(self):
        return datetime.fromtimestamp(self.matchInfo.gameStartMillis/1000.0)
    
    def get_player(self, **kw):
        return next((p for p in self.players if p.puuid == id), None)
    
    def get_player_by_name(self, name):
        for p in self.players:
            if f"{p.gameName}#{p.tagLine}" == name:
                return p
        
        return None

    def get_round(self, num):
        return next((r for r in self.roundResults if r.roundNum == num), None)
    
    def get_winner(self):
        return next((t for t in self.teams if t.won == True), None)


class MatchlistEntryDTO(DTO):
    def __init__(self, obj, handle):
        self._json = obj
        self._handle = handle
        self.id = obj["matchId"]
        self.set_attributes(obj)

    def get(self):
        match = self._handle.call("GET", "match", matchID=self.id)

        return MatchDTO(match)


class MatchlistDTO(DTO):
    def __init__(self, obj, handle):
        self._json = obj
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