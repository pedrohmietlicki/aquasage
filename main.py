import schedule
from src.services import RiverLevelService
import time




def main():
    riverLevelService = RiverLevelService()
    schedule.every(1).hour.do(riverLevelService.getData())
    while True:
        schedule.run_pending()
        time.sleep(1800)