import schedule
from src.services import RiverLevelService





def main():
    riverLevelService = RiverLevelService()
    schedule.every(1).hour.do(riverLevelService.getData())
   