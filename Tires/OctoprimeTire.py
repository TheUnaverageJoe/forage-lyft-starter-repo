from Tires.ITire import ITire

class OctoprimeTire(ITire):
    def __init__(self, tires_array: list) -> None:
        self.__tires = tires_array

    def needs_service(self) -> bool:
        total = 0
        for tire in self.__tires:
            total += tire
        if total >= 3:
            return True
        return False