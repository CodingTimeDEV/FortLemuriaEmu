from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EMonsterCategory import EMonsterCategory
from serverfiles.types.enums.EMonsterSpecies import EMonsterSpecies
from serverfiles.types.enums.EMonsterVoiceCategory import EMonsterVoiceCategory

class CMonsterModel(CTypeImplBaseClass):
    m_iMonsterId: int
    m_szName: str
    m_iEvolutionStep: int
    m_iBlowRate: int
    m_eMonsterCategory: EMonsterCategory
    m_eMonsterSpecies: EMonsterSpecies
    m_eMonsterVoiceCategory: EMonsterVoiceCategory
    m_iModelId: int
    m_iMotionId: int
    m_iSeqId: int

    def toJSON(self) -> dict[str, Any]:
        return {
            "monsterId": self.m_iMonsterId,
            "name": self.m_szName,
            "evolutionStep": self.m_iEvolutionStep,
            "blowRate": self.m_iBlowRate,
            "category": self.m_eMonsterCategory.value,
            "species": self.m_eMonsterSpecies.value,
            "voiceCategory": self.m_eMonsterVoiceCategory.value,
            "modelId": self.m_iModelId,
            "motionId": self.m_iMotionId,
            "sequenceId": self.m_iSeqId
        }