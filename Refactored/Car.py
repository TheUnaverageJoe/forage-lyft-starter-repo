from IServicable import IServicable
from IBattery import IBattery
from IEngine import IEngine

class Car(IServicable):
    def __init__(self, engine: IEngine, battery: IBattery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        pass
