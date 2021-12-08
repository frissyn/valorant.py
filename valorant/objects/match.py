import typing as t

from .dto import DTO

from .player import PlayerDTO
from .player import LocationDTO
from .player import PlayerStatsDTO
from .player import PlayerLocationsDTO

from datetime import datetime


class CoachDTO(DTO):
    puuid: str
    teamId: str

    def __getattribute__(self, name):
        return super(CoachDTO, self).__getattribute__(name)


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

    def __getattribute__(self, name):
        return super(MatchInfoDTO, self).__getattribute__(name)


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

    def __getattribute__(self, name):
        return super(MatchlistEntryDTO, self).__getattribute__(name)


class MatchlistDTO(DTO):
    puuid: str
    history: t.Iterable[MatchlistEntryDTO]

    def __init__(self, obj, handle):
        self._json = obj
        self.set_attributes(obj)

        for i, e in enumerate(self.history):
            self.history[i] = MatchlistEntryDTO(e, handle)

    def __getattribute__(self, name):
        return super(MatchlistDTO, self).__getattribute__(name)


class TeamDTO(DTO):
    teamId: str
    won: bool
    roundsPlayed: int
    roundsWon: int
    numPoints: int

    def __getattribute__(self, name):
        return super(TeamDTO, self).__getattribute__(name)


class RoundResultDTO(DTO):
    roundNum: int
    roundResult: str
    roundCeremony: str
    winningTeam: str
    bombPlanter: str
    bombDefuser: str
    plantRoundTime: int
    plantPlayerLocations: t.Optional[t.Iterable[PlayerLocationsDTO]]
    plantLocation: LocationDTO
    plantSite: t.Optional[str]
    defuseRoundTime: int
    defusePlayerLocations: t.Optional[t.Iterable[PlayerLocationsDTO]]
    defuseLocation: LocationDTO
    playerStats: t.Iterable[PlayerStatsDTO]
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
        
        self.playerStats = [PlayerStatsDTO(s) for s in obj["playerStats"]]

    def __getattribute__(self, name):
        return super(RoundResultDTO, self).__getattribute__(name)


class MatchDTO(DTO):
    matchInfo: MatchInfoDTO
    players: t.Iterable[PlayerDTO]
    coaches: t.Iterable[CoachDTO]
    teams: t.Iterable[TeamDTO]
    roundResults: t.Iterable[RoundResultDTO]

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
