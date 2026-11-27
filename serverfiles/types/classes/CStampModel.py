from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass

class CStampModel(CTypeImplBaseClass):
    m_iStampId: int
    m_strName: str
    m_strDescription: str
    m_strText: str
    m_strImage: str
    m_strSeName: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "stampId": self.m_iStampId,
            "name": self.m_strName,
            "description": self.m_strDescription,
            "text": self.m_strText,
            "image": self.m_strImage,
            "seName": self.m_strSeName
        }
    