from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EGender import EGender
from serverfiles.types.enums.ECharacterBodyShape import ECharacterBodyShape

class CCharacterProfileModel(CTypeImplBaseClass):
    m_iCharacterProfileId: int
    m_strName: str
    m_eGender: EGender
    m_eBodyShape: ECharacterBodyShape
    m_strVoice: str
    m_iPersonality: int
    m_strAmmoName: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "characterProfileId": self.m_iCharacterProfileId,
            "name": self.m_strName,
            "gender": self.m_eGender.name,
            "bodyShape": self.m_eBodyShape.name,
            "voice": self.m_strVoice,
            "personality": self.m_iPersonality,
            "ammoName": self.m_strAmmoName
        }