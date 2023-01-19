from datetime import datetime
from Engines.SternmanEngine import SternmanEngine
from Engines.CapuletEngine import CapuletEngine
from Engines.WilloughbyEngine import WilloughbyEngine
from Batteries.SpindlerBattery import SpindlerBattery
from Batteries.NubbinBattery import NubbinBattery
from Tires.OctoprimeTire import OctoprimeTire
from Tires.CarriganTire import CarriganTire
from Car import Car

class CarFactory():
    def create_calliope(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int, tire_wear: list[4]) -> Car:
        return Car(CapuletEngine(last_service_milage, current_milage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))

    def create_glissade(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int, tire_wear: list[4]) -> Car:
        return Car(WilloughbyEngine(last_service_milage, current_milage), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))

    def create_palindrome(self, current_date: datetime, last_service_date: datetime, warning_light_on: bool, tire_wear: list[4]) -> Car:
        return Car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date), CarriganTire(tire_wear))

    def create_rorschach(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int, tire_wear: list[4]) -> Car:
        return Car(WilloughbyEngine(last_service_milage, current_milage), NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))

    def create_thovex(self, current_date: datetime, last_service_date: datetime, current_milage: int, last_service_milage: int, tire_wear: list[4]) -> Car:
        return Car(CapuletEngine(last_service_milage, current_milage), NubbinBattery(last_service_date, current_date), OctoprimeTire(tire_wear))
