import typing as t

from .dto import DTO
from ..lexicon import Lex


class AbilityCastsDTO(DTO):
    totalCasts: int
    grenadeCasts: int
    ability1Casts: int
    ability2Casts: int
    ultimateCasts: int

    def __init__(self, obj):
        super().__init__(obj)

        self.totalCasts = (
            self.grenadeCasts
            + self.ability1Casts
            + self.ability2Casts
            + self.ultimateCasts
        )


class LocationDTO(DTO):
    x: int
    y: int


class PlayerLocationsDTO(DTO):
    puuid: str
    viewRadians: float
    location: LocationDTO


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

        self.abilityCasts = AbilityCastsDTO.optional(obj.get("abilityCasts"))

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

        self.stats = PlayerDTO.optional(obj.get("stats"))

        if obj.get("competitiveTier"):
            self.rank = Lex.RANKS[self.competitiveTier]
        else:
            self.rank = "Unrated"
