from .dto import DTO

from .match import MatchlistDTO


class AccountDTO(DTO):
    puuid: str
    gameName: str
    tagLine: str

    def __init__(self, obj, handle):
        self._json = obj
        self.handle = handle
        self.set_attributes(obj)

    def matchlist(self) -> MatchlistDTO:
        """Get a :class:`MatchlistDTO` of the most recent matches played
        by this account.

        :rtype: MatchlistDTO
        """
        l = self.handle.call("GET", "matchlists", puuid=self.puuid)

        return MatchlistDTO(l, self.handle)
