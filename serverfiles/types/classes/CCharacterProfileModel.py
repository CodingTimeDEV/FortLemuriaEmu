from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EGender import EGender
from serverfiles.types.enums.ECharacterBodyShape import ECharacterBodyShape

class CCharacterProfileModel(CTypeImplBaseClass):
    m_iCharacterProfileId: int
    m_szName: str
    m_eGender: EGender
    m_eBodyShape: ECharacterBodyShape
    m_szVoice: str
    m_iPersonality: int
    m_szAmmoName: str

    def toJSON(self) -> dict[str, Any]:
        return {
            "characterProfileId": self.m_iCharacterProfileId,
            "name": self.m_szName,
            "gender": self.m_eGender.value,
            "bodyShape": self.m_eBodyShape.value,
            "voice": self.m_szVoice,
            "personality": self.m_iPersonality,
            "ammoName": self.m_szAmmoName
        }