import json
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EUtilityTicketType import EUtilityTicketType

class CUtilityTicketModel(CTypeImplBaseClass):
    m_iUtilityTicketId: int
    m_strName: str
    m_strDescription: str
    m_eUtilityTicketType: EUtilityTicketType
    m_iDuration: int
    m_iValue: int

    def toJSON(self) -> str:
        return json.dumps({
            "UtilityTicketId": self.m_iUtilityTicketId,
            "Name": self.m_strName,
            "Description": self.m_strDescription,
            "Type": self.m_eUtilityTicketType.value,
            "Duration": self.m_iDuration,
            "Value": self.m_iValue
        })