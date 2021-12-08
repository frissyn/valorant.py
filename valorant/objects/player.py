import typing as t

from .dto import DTO


class AbilityCastsDTO(DTO):
    totalCasts: int
    grenadeCasts: int
    ability1Casts: int
    ability2Casts: int
    ultimateCasts: int

    def __init__(self, obj):
        super().__init__(obj)

        self.totalCasts = (
            self.grenadeCasts +
            self.ability1Casts +
            self.ability2Casts +
            self.ultimateCasts
        )

    def __getattribute__(self, name):
        return super(AbilityCastsDTO, self).__getattribute__(name)


class LocationDTO(DTO):
    x: int
    y: int

    def __getattribute__(self, name):
        return super(LocationDTO, self).__getattribute__(name)


class PlayerLocationsDTO(DTO):
    puuid: str
    viewRadians: float
    location: LocationDTO

    def __getattribute__(self, name):
        return super(PlayerLocationsDTO, self).__getattribute__(name)


class PlayerStatsDTO(DTO):
    score: int
    kd: t.Optional[int]
    kda: t.Optional[int]
    averageScore: t.Optional[int]
    roundsPlayed: int
    kills: int
    deaths: int
    assists: int
    playtimeMillis: int
    abilityCasts: t.Optional[AbilityCastsDTO]

    def __init__(self, obj):
        super().__init__(obj)

        if obj.get("abilityCasts"):
            self.abilityCasts = AbilityCastsDTO(obj["abilityCasts"])
        else:
            self.abilityCasts = None

        try:
            self.kd = obj["kills"] / obj["deaths"]
        except ZeroDivisionError:
            self.kd = obj["kills"]
        except KeyError:
            self.kd = None

        try:
            self.kda = (obj["kills"] + obj["assists"]) / obj["deaths"]
        except ZeroDivisionError:
            self.kda = self.kills + self.assists
        except KeyError:
            self.kda = None

        try:
            self.averageScore = obj["score"] / obj["roundsPlayed"]
        except KeyError:
            self.averageScore = None

    def __getattribute__(self, name):
        return super(PlayerStatsDTO, self).__getattribute__(name)


class PlayerDTO(DTO):
    puuid: str
    gameName: str
    tagLine: str
    teamId: str
    partyId: str
    characterId: str
    stats: t.Optional[PlayerStatsDTO]
    competitiveTier: int
    playerCard: str
    playerTitle: str

    def __init__(self, obj):
        super().__init__(obj)

        if obj.get("stats"):
            self.stats = PlayerStatsDTO(obj["stats"])
        else:
            self.stats = None

    def __getattribute__(self, name):
        return super(PlayerDTO, self).__getattribute__(name)
