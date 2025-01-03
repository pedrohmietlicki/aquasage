import requests
import json 
from ..utils import datetime_to_seconds
from ..repositories import InfluxRepository
class RiverLevelService():
    baseUrl = "https://nivelguaiba.com.br/portoalegre.1day.json"
    def getData(self):
        response = requests.get(self.baseUrl)
        levels = response.json()
        influxRepository = InfluxRepository()
        for timestamp, level in levels.items():
            timestamp = datetime_to_seconds(timestamp)
            influxRepository.saveData(timestamp,level)
            
