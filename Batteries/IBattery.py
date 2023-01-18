from abc import ABC, abstractmethod


class IBattery(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
