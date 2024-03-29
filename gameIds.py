import requests
import json
import csv

class Player:


    def __init__(self, nick, api_key):
        self.nick = nick
        self.api_key = api_key
        nome_arquivo = f'.\dados\{self.nick}.csv'
        headers = ['championName', 'kills', 'assists', 'deaths', 'wardsPlaced', 'wardsKilled', 'win', 'timePlayed']
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(headers)

    def __str__(self):
        return "https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"+self.nick+"?api_key="+self.api_key

    def Data(self):
        request_player = requests.get(self.__str__())
        player_data = request_player.json()
        return player_data

    def Id(self):
        playerData = self.Data()
        player_id = playerData["accountId"]
        return player_id

    def puuId(self):
        playerData = self.Data()
        player_id = playerData["puuid"]
        return player_id