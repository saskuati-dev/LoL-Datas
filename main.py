from gameIds import *
from matches import *


token ="" #api key
nick = "" #your nickname here
regiao = "" #server

RiotPlayer = Player(nick, token)
LoLMatches = Match(RiotPlayer.puuId(), regiao, token)

Ids = LoLMatches.MatchId()

print(LoLMatches.MatchData(Ids[0]))

print(type(Ids))