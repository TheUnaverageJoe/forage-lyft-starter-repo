from Engines.IEngine import IEngine

class WilloughbyEngine(IEngine):
    def __init__(self, last_service_milage: int, current_milage: int) -> None:
        self.__last_service_milage = last_service_milage
        self.__current_milage = current_milage
    
    def needs_service(self) -> bool:
        if self.__current_milage - self.__last_service_milage >= 60000:
            return True
        else:
            return False