from abc import ABC, abstractmethod

class ITire(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass