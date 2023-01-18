from IBattery import IBattery
from datetime import datetime

class SpindlerBattery(IBattery):
    def __init__(self, last_service_date: datetime, current_date: datetime) -> None:
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    def needs_service(self) -> bool:
        if self.__last_service_date.replace(year=self.__last_service_date.year+2) >= self.__current_date:
            return True
        else:
            return False