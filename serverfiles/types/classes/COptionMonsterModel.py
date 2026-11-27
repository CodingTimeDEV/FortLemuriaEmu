from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.ERarity import ERarity
from serverfiles.types.enums.EOptionMonsterRole import EOptionMonsterRole
from serverfiles.types.enums.EElementalType import EElementalType
from serverfiles.types.classes.COptionMonsterAiModel import COptionMonsterAiModel

class COptionMonsterModel(CTypeImplBaseClass):
    m_iOptionMonsterId: int
    m_strName: str
    m_iIndex: int
    m_iMonsterId: int
    m_iIconId: int
    m_eRarity: ERarity
    m_flRadius: float
    m_flScaleFactor: float
    m_eRole: EOptionMonsterRole
    m_iPrice: int
    m_iBaseAttack: int
    m_eElementalType: EElementalType
    m_iBaseElementalPoint: int
    m_iBaseEvaluation: int
    m_iOptionMonsterSkillId: int
    m_iHateId: int
    m_OptionMonsterAiModel: COptionMonsterAiModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "optionMonsterId": self.m_iOptionMonsterId,
            "name": self.m_strName,
            "index": self.m_iIndex,
            "monsterId": self.m_iMonsterId,
            "iconId": self.m_iIconId,
            "rarity": self.m_eRarity.value,
            "radius": self.m_flRadius,
            "scaleFactor": self.m_flScaleFactor,
            "role": self.m_eRole.value,
            "price": self.m_iPrice,
            "baseAttack": self.m_iBaseAttack,
            "elementalType": self.m_eElementalType.value,
            "baseElementalPoint": self.m_iBaseElementalPoint,
            "baseEvaluation": self.m_iBaseEvaluation,
            "optionMonsterSkillId": self.m_iOptionMonsterSkillId,
            "hateId": self.m_iHateId,
            "optionMonsterAiModel": self.m_OptionMonsterAiModel.toJSON()
        }
