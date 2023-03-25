import requests
import json

class Match:

    def __init__(self, puuId, region, api_key):
        self.puuId = puuId
        self.region = region
        self.api_key = api_key

    def MatchId(self):
        url = "https://"+self.region+".api.riotgames.com/lol/match/v5/matches/by-puuid/"+self.puuId+"/ids?start=0&count=20&api_key="+self.api_key
        req = requests.get(url)
        matches = req.json()
        return matches

    def MatchData(self, id):
        url = "https://"+self.region+".api.riotgames.com/lol/match/v5/matches/"+id+"?api_key="+self.api_key
        req = requests.get(url)
        matchData= req.json()
        for i in range(10):
            if matchData['metadata']['participants'][i] == self.puuId:
                return  matchData['info']['participants'][i]

