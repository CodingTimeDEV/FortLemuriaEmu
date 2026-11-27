from typing import Any
from serverfiles.types.classes.CModel import CModel
from serverfiles.types.classes.COptionMonsterSkillModel import COptionMonsterSkillModel
from serverfiles.types.classes.CModifiedQuestModel import CModifiedQuestModel
from serverfiles.types.classes.COptionMonsterModel import COptionMonsterModel
from serverfiles.types.classes.CMonsterModel import CMonsterModel
from serverfiles.types.classes.CMonsterDescriptionModel import CMonsterDescriptionModel

class CMonsterIndexOptionMonsterDetailResponse(CModel):
    m_OptionMonster: COptionMonsterModel
    m_Monster: CMonsterModel
    m_arrDropQuests: list[CModifiedQuestModel]
    m_Description: CMonsterDescriptionModel
    m_OptionMonsterSkill: COptionMonsterSkillModel

    def toJSON(self) -> dict[str, Any]:
        return {
            "optionMonster": self.m_OptionMonster.toJSON(),
            "monster": self.m_Monster.toJSON(),
            "dropQuests": [dq.toJSON() for dq in self.m_arrDropQuests],
            "description": self.m_Description.toJSON(),
            "optionMonsterSkill": self.m_OptionMonsterSkill.toJSON()
        }