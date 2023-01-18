from abc import ABC, abstractmethod

class IServicable(ABC):
    """Interface to be inhierited for any servicable vehicle"""
    @abstractmethod
    def needs_service(self) -> bool:
        pass
