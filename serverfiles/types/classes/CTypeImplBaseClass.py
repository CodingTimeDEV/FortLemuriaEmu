from abc import ABC, abstractmethod

class CTypeImplBaseClass(ABC):

    @abstractmethod
    def toJSON(self) -> str:
        pass