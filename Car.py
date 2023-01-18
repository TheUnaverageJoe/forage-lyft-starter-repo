from IServicable import IServicable
from Batteries.IBattery import IBattery
from Engines.IEngine import IEngine

class Car(IServicable):
    def __init__(self, engine: IEngine, battery: IBattery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        if self.engine.needs_service() or self.battery.needs_service():
            return True
        else:
            return False
