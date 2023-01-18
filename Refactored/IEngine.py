from abc import ABC, abstractmethod

class IEngine(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass
