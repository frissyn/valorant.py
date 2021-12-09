import typing as t

from .dto import DTO

from .player import PlayerDTO
from .player import LocationDTO
from .player import PlayerStatsDTO
from .player import PlayerLocationsDTO

from datetime import datetime


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

    def get_time_since_game_start(self) -> datetime:
        return datetime.fromtimestamp(self.timeSinceGameStartMillis / 1000.0)

    def get_time_since_round_start(self) -> datetime:
        return datetime.fromtimestamp(self.timeSinceRoundStartMillis / 1000.0)


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


class MatchlistEntryDTO(DTO):
    matchId: str
    gameStartMillis: int
    teamId: str

    def __init__(self, obj, handle):
        self._json = obj
        self._handle = handle
        self.id = obj["matchId"]
        self.set_attributes(obj)

    def get(self):
        match = self._handle.call("GET", "match", matchID=self.id)

        return MatchDTO(match)

    def get_timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.gameStartMillis / 1000.0)


class MatchlistDTO(DTO):
    puuid: str
    history: t.List[MatchlistEntryDTO]

    def __init__(self, obj, handle):
        super().__init__(obj)

        self.history = [MatchlistEntryDTO(e, handle) for e in obj["history"]]


class PlayerRoundStatsDTO(DTO):
    puuid: str
    kills: t.List[t.Any]
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

        if obj.get("plantLocation"):
            self.plantLocation = LocationDTO(obj["plantLocation"])
        else:
            self.plantLocation = None

        if obj.get("defuseLocation"):
            self.defuseLocation = LocationDTO(obj["defuseLocation"])
        else:
            self.defuseLocation = None

        if obj.get("plantPlayerLocations"):
            self.plantPlayerLocations = [
                PlayerLocationsDTO(l) for l in obj["plantPlayerLocations"]
            ]
        else:
            self.plantPlayerLocations = None

        if obj.get("defusePlayerLocations"):
            self.defusePlayerLocations = [
                PlayerLocationsDTO(l) for l in obj["defusePlayerLocations"]
            ]
        else:
            self.defusePlayerLocations = None

        self.playerStats = [PlayerRoundStatsDTO(s) for s in obj["playerStats"]]


class MatchDTO(DTO):
    matchInfo: MatchInfoDTO
    players: t.List[PlayerDTO]
    coaches: t.List[CoachDTO]
    teams: t.List[TeamDTO]
    roundResults: t.List[RoundResultDTO]

    def __init__(self, obj):
        self._json = obj
        self.id = obj["matchInfo"]["matchId"]

        self.matchInfo = MatchInfoDTO(obj["matchInfo"])
        self.players = [PlayerDTO(p) for p in obj["players"]]
        self.coaches = [CoachDTO(c) for c in obj["coaches"]]
        self.teams = [TeamDTO(t) for t in obj["teams"]]
        self.roundResults = [RoundResultDTO(r) for r in obj["roundResults"]]

    def get_team(self, name) -> t.Optional[TeamDTO]:
        return next((t for t in self.teams if t.teamId == name), None)

    def get_timestamp(self) -> datetime:
        return datetime.fromtimestamp(self.matchInfo.gameStartMillis / 1000.0)

    def get_player(self, **kw) -> t.Optional[PlayerDTO]:
        return next((p for p in self.players if p.puuid == id), None)

    def get_player_by_name(self, name) -> t.Optional[PlayerDTO]:
        for p in self.players:
            if f"{p.gameName}#{p.tagLine}" == name:
                return p

    def get_round(self, num) -> t.Optional[RoundResultDTO]:
        return next((r for r in self.roundResults if r.roundNum == num), None)

    def get_winner(self) -> t.Optional[TeamDTO]:
        return next((t for t in self.teams if t.won == True), None)
