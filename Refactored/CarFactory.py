from datetime import datetime
from SternmanEngine import SternmanEngine
from CapuletEngine import CapuletEngine
from WilloughbyEngine import WilloughbyEngine
from SpindlerBattery import SpindlerBattery
from NubbinBattery import NubbinBattery
from Car import Car

class CarFactory():
    def create_calliope(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int) -> Car:
        return Car(CapuletEngine(last_service_milage, current_milage), SpindlerBattery(last_service_date, current_date))
    def create_glissade(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int) -> Car:
        return Car(WilloughbyEngine(last_service_milage, current_milage), SpindlerBattery(last_service_date, current_date))
    def create_palindrome(self, current_date: datetime, last_service_date: datetime, warning_light_on: bool) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date))
    def create_rorschach(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int) -> Car:
        return Car(WilloughbyEngine(last_service_milage, current_milage), NubbinBattery(last_service_date, current_date))
    def create_thovex(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int) -> Car:
        return Car(CapuletEngine(last_service_milage, current_milage), NubbinBattery(last_service_date, current_date))