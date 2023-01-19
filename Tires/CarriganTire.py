from Tires.ITire import ITire

class CarriganTire(ITire):
    def __init__(self, tires_array: list) -> None:
        self.__tires = tires_array

    def needs_service(self) -> bool:
        for tire in self.__tires:
            if tire >= 0.9:
                return True
        return False
