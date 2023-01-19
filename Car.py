from IServicable import IServicable
from Batteries.IBattery import IBattery
from Engines.IEngine import IEngine
from Tires.ITire import ITire

class Car(IServicable):
    def __init__(self, engine: IEngine, battery: IBattery, tires: ITire = None) -> None:
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service():
            return True
        else:
            return False
