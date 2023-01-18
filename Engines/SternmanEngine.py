from Engines.IEngine import IEngine

class SternmanEngine(IEngine):
    def __init__(self, warning_light_on: bool) -> None:
        self.__warning_light_on = warning_light_on
    
    def needs_service(self) -> bool:
        if self.__warning_light_on:
            return True
        else:
            return False