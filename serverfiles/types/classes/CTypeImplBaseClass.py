from typing import Any
from abc import ABC, abstractmethod
class CTypeImplBaseClass(ABC):

    @abstractmethod
    def toJSON(self) -> dict[str, Any]:
        pass