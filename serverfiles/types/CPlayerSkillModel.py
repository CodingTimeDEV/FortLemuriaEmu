import json
from serverfiles.types.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.EMountType import EMountType
from serverfiles.types.EComboCommandType import EComboCommandType
from serverfiles.types.ESkillStyle import ESkillStyle
from serverfiles.types.CPlayerSkillStatusModel import CPlayerSkillStatusModel
from serverfiles.types.CPlayerSkillModuleModel import CPlayerSkillModuleModel

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

    def toJSON(self) -> str:
        return json.dumps({
            "PlayerSkillId": self.m_iPlayerSkillId,
            "Name": self.m_strName,
            "Description": self.m_strDescription,
            "MountType": self.m_eMountType.value,
            "CommandType": self.m_eComboCommandType.value,
            "Style": self.m_eSkillStyle.value,
            "EasyBreakMonsterIds": self.m_arrEasyBreakMonsterIds,
            "IsAttackSpeedUpEnable": self.m_bIsAttackSpeedUpEnable,
            "Statuses": [status.toJSON() for status in self.m_arrPlayerSkillStatusModel],
            "Module": self.m_PlayerSkillModule.toJSON()
        })