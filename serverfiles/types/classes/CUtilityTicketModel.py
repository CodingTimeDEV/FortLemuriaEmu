from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EUtilityTicketType import EUtilityTicketType

class CUtilityTicketModel(CTypeImplBaseClass):
    m_iUtilityTicketId: int
    m_strName: str
    m_strDescription: str
    m_eUtilityTicketType: EUtilityTicketType
    m_iDuration: int
    m_iValue: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "utilityTicketId": self.m_iUtilityTicketId,
            "name": self.m_strName,
            "description": self.m_strDescription,
            "type": self.m_eUtilityTicketType.value,
            "duration": self.m_iDuration,
            "value": self.m_iValue
        }