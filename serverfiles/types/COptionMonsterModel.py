import json

from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.ERarity import ERarity
from serverfiles.types.EOptionsMonsterRole import EOptionsMonsterRole
from serverfiles.types.EElementalType import EElementalType
from serverfiles.types.COptionMonsterAiModel import COptionMonsterAiModel

class COptionMonsterModel(CTypeImplBaseClass):
    m_iOptionMonsterId: int
    m_strName: str
    m_iIndex: int
    m_iMonsterId: int
    m_iIconId: int
    m_eRarity: ERarity
    m_flRadius: float
    m_flScaleFactor: float
    m_eRole: EOptionsMonsterRole
    m_iPrice: int
    m_iBaseAttack: int
    m_eElementalType: EElementalType
    m_iBaseElementalPoint: int
    m_iBaseEvaluation: int
    m_iOptionMonsterSkillId: int
    m_iHateId: int
    m_OptionMonsterAiModel: COptionMonsterAiModel

    def toJSON(self) -> str:
        return json.dumps({
            "OptionMonsterId": self.m_iOptionMonsterId,
            "Name": self.m_strName,
            "Index": self.m_iIndex,
            "MonsterId": self.m_iMonsterId,
            "IconId": self.m_iIconId,
            "Rarity": self.m_eRarity.value,
            "Radius": self.m_flRadius,
            "ScaleFactor": self.m_flScaleFactor,
            "Role": self.m_eRole.value,
            "Price": self.m_iPrice,
            "BaseAttack": self.m_iBaseAttack,
            "ElementalType": self.m_eElementalType.value,
            "BaseElementalPoint": self.m_iBaseElementalPoint,
            "BaseEvaluation": self.m_iBaseEvaluation,
            "OptionMonsterSkillId": self.m_iOptionMonsterSkillId,
            "HateId": self.m_iHateId,
            "OptionMonsterAiModel": self.m_OptionMonsterAiModel.toJSON()
        })
