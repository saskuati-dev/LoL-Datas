from gameIds import *
from matches import *


token ="" #api key
nick = "" #your nickname here
regiao = "" #server
numeroPartidas = 50

RiotPlayer = Player(nick, token)
LoLMatches = Match(RiotPlayer.puuId(), regiao, token, nick, numeroPartidas)

Ids = LoLMatches.MatchId() #return an array

for i in range(len(Ids)):
    LoLMatches.MatchData(Ids[i])

print("Finished process")
