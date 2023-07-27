import requests
import json
import csv
import pandas as pd

class Match:

    def __init__(self, puuId, region, api_key, nick, ptd):
        self.puuId = puuId
        self.region = region
        self.api_key = api_key
        self.nick = nick
        self.ptd = ptd

    def MatchId(self):
        url = "https://"+self.region+".api.riotgames.com/lol/match/v5/matches/by-puuid/"+self.puuId+"/ids?start=0&count="+str(self.ptd)+"&api_key="+self.api_key
        req = requests.get(url)
        matches = req.json()
        return matches

    def MatchData(self, id):
        url = "https://"+self.region+".api.riotgames.com/lol/match/v5/matches/"+id+"?api_key="+self.api_key
        req = requests.get(url)
        matchData= req.json()
        for i in range(10):
            if matchData['metadata']['participants'][i] == self.puuId:
                teste = matchData['info']['participants'][i]

        df = pd.DataFrame(teste)
        df1 = df[['championName', 'kills', 'assists', 'deaths', 'wardsPlaced', 'wardsKilled', 'win', 'timePlayed']]
        
        df2 = df1.drop(df1.index[1:])
        file = f'.\dados\{self.nick}.csv'
        df2.to_csv(file, mode='a', index=False, header=False)


