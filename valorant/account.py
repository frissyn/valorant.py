from .lexicon import Lex

from .objects import DTO
from .objects import MatchlistDTO

from .caller import WebCaller

class Account(DTO):
    def __init__(self, obj, handle: WebCaller):
        self.json = obj
        self.handle = handle
        self.set_attributes(obj)

    def matchlist(self):
        l = self.handle.call("GET", "matchlists", puuid=self.puuid)

        return MatchlistDTO(l)
