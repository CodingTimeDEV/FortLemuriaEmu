import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EMonsterCategory import EMonsterCategory
from serverfiles.types.EMonsterSpecies import EMonsterSpecies
from serverfiles.types.EMonsterVoiceCategory import EMonsterVoiceCategory

class CMonsterModel(CTypeImplBaseClass):
    m_iMonsterId: int
    m_strName: str
    m_iEvolutionStep: int
    m_iBlowRate: int
    m_eMonsterCategory: EMonsterCategory
    m_eMonsterSpecies: EMonsterSpecies
    m_eMonsterVoiceCategory: EMonsterVoiceCategory
    m_iModelId: int
    m_iMotionId: int
    m_iSeqId: int

    def toJSON(self):
        return json.dumps({
            "MonsterId": self.m_iMonsterId,
            "Name": self.m_strName,
            "EvolutionStep": self.m_iEvolutionStep,
            "BlowRate": self.m_iBlowRate,
            "MonsterCategory": self.m_eMonsterCategory.value,
            "MonsterSpecies": self.m_eMonsterSpecies.value,
            "MonsterVoiceCategory": self.m_eMonsterVoiceCategory.value,
            "ModelId": self.m_iModelId,
            "MotionId": self.m_iMotionId,
            "SequenceId": self.m_iSeqId
        })