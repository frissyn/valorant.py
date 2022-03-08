from __future__ import annotations

import typing as t
from datetime import datetime

from .content import ContentList
from .dto import DTO
from .player import PlayerDTO, LocationDTO, PlayerStatsDTO, PlayerLocationsDTO


class AbilityDTO(DTO):
    grenadeEffects: str
    ability1Effects: str
    ability2Effects: str
    ultimateEffects: str


class CoachDTO(DTO):
    puuid: str
    teamId: str


class DamageDTO(DTO):
    receiver: str
    damage: int
    legshots: int
    bodyshots: int
    headshots: int


class FinishingDamageDTO(DTO):
    damageType: str
    damageItem: str
    isSecondaryFireMode: bool


class EconomyDTO(DTO):
    loadoutValue: int
    weapon: str
    armor: str
    remaining: int
    spent: int


class KillDTO(DTO):
    timeSinceGameStartMillis: int
    timeSinceRoundStartMillis: int
    killer: str
    victim: str
    victimLocation: LocationDTO
    assistants: t.List[str]
    playerLocations: t.List[PlayerLocationsDTO]
    finishingDamage: FinishingDamageDTO

    def __init__(self, obj):
        super().__init__(obj)

        self.timeSinceGameStart = datetime.fromtimestamp(
            self.timeSinceGameStartMillis / 1000.0
        )
        self.timeSinceRoundStart = datetime.fromtimestamp(
            self.timeSinceRoundStartMillis / 1000.0
        )


class TeamDTO(DTO):
    teamId: str
    won: bool
    roundsPlayed: int
    roundsWon: int
    numPoints: int


class MatchInfoDTO(DTO):
    matchId: str
    mapId: str
    gameLengthMillis: int
    gameStartMillis: int
    provisioningFlowId: str
    isCompleted: bool
    customGameName: str
    queueId: str
    gameMode: str
    isRanked: bool
    seasonId: str


class MatchlistDTO(DTO):
    puuid: str
    history: t.List[MatchlistEntryDTO]

    def __init__(self, obj, handle):
        super().__init__(obj)

        self.history = ContentList(MatchlistEntryDTO(e, handle) for e in obj["history"])


class MatchlistEntryDTO(DTO):
    matchId: str
    gameStartMillis: int
    teamId: str

    def __init__(self, obj, handle):
        self._json = obj
        self._handle = handle
        self.id = obj["matchId"]
        self.set_attributes(obj)

    def get(self) -> MatchDTO:
        match = self._handle.call("GET", "match", matchID=self.id)

        return MatchDTO(match)

    def timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.gameStartMillis / 1000.0)


class PlayerRoundStatsDTO(DTO):
    puuid: str
    kills: t.List[KillDTO]
    damage: t.List[DamageDTO]
    score: int
    economy: EconomyDTO
    ability: AbilityDTO

    def __init__(self, obj):
        super().__init__(obj)

        self.economy = EconomyDTO(obj["economy"])
        self.ability = AbilityDTO(obj["ability"])


class RoundResultDTO(DTO):
    roundNum: int
    roundResult: str
    roundCeremony: str
    winningTeam: str
    bombPlanter: str
    bombDefuser: str
    plantRoundTime: int
    plantPlayerLocations: t.Optional[t.List[PlayerLocationsDTO]]
    plantLocation: LocationDTO
    plantSite: t.Optional[str]
    defuseRoundTime: int
    defusePlayerLocations: t.Optional[t.List[PlayerLocationsDTO]]
    defuseLocation: LocationDTO
    playerStats: t.List[PlayerStatsDTO]
    roundResultCode: str

    def __init__(self, obj):
        super().__init__(obj)

        self.plantLocation = LocationDTO.optional(obj.get("plantLocation"))
        self.defuseLocation = LocationDTO.optional(obj.get("defuseLocation"))

        if obj.get("plantPlayerLocations"):
            self.plantPlayerLocations = ContentList(
                PlayerLocationsDTO(l) for l in obj["plantPlayerLocations"]
            )
        else:
            self.plantPlayerLocations = None

        if obj.get("defusePlayerLocations"):
            self.defusePlayerLocations = ContentList(
                PlayerLocationsDTO(l) for l in obj["defusePlayerLocations"]
            )
        else:
            self.defusePlayerLocations = None

        self.playerStats = ContentList(
            PlayerRoundStatsDTO(s) for s in obj["playerStats"]
        )


class MatchDTO(DTO):
    matchInfo: MatchInfoDTO
    players: t.List[PlayerDTO]
    coaches: t.List[CoachDTO]
    teams: t.List[TeamDTO]
    timestamp: datetime
    roundResults: t.List[RoundResultDTO]

    def __init__(self, obj):
        self._json = obj
        self.id = obj["matchInfo"]["matchId"]

        self.matchInfo = MatchInfoDTO(obj["matchInfo"])
        self.players = ContentList(PlayerDTO(p) for p in obj["players"])
        self.coaches = ContentList(CoachDTO(c) for c in obj["coaches"])
        self.teams = ContentList(TeamDTO(t) for t in obj["teams"])
        self.roundResults = ContentList(RoundResultDTO(r) for r in obj["roundResults"])

        self.datetime = datetime.fromtimestamp(self.matchInfo.gameStartMillis / 1000.0)
