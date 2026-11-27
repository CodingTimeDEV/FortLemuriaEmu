from typing import Any
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EMountType import EMountType
from serverfiles.types.enums.EComboCommandType import EComboCommandType
from serverfiles.types.enums.ESkillStyle import ESkillStyle
from serverfiles.types.classes.CPlayerSkillStatusModel import CPlayerSkillStatusModel
from serverfiles.types.classes.CPlayerSkillModuleModel import CPlayerSkillModuleModel

class CPlayerSkillModel(CTypeImplBaseClass):
    m_iPlayerSkillId: int
    m_strName: str
    m_strDescription: str
    m_eMountType: EMountType
    m_eComboCommandType: EComboCommandType
    m_eSkillStyle: ESkillStyle
    m_arrEasyBreakMonsterIds: list[int]
    m_bIsAttackSpeedUpEnable: bool
    m_arrPlayerSkillStatusModel: list[CPlayerSkillStatusModel]
    m_PlayerSkillModule: CPlayerSkillModuleModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "playerSkillId": self.m_iPlayerSkillId,
            "name": self.m_strName,
            "description": self.m_strDescription,
            "mountType": self.m_eMountType.value,
            "commandType": self.m_eComboCommandType.value,
            "style": self.m_eSkillStyle.value,
            "easyBreakMonsterIds": self.m_arrEasyBreakMonsterIds,
            "isAttackSpeedUpEnable": self.m_bIsAttackSpeedUpEnable,
            "statuses": [status.toJSON() for status in self.m_arrPlayerSkillStatusModel],
            "module": self.m_PlayerSkillModule.toJSON()
        }