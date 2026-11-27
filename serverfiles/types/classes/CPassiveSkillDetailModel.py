import json
from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.enums.EPassiveSkillType import EPassiveSkillType
from serverfiles.types.enums.EPassiveSkillTargetType import EPassiveSkillTargetType

class CPassiveSkillDetailModel(CTypeImplBaseClass):
    m_ePassiveSkillType: EPassiveSkillType
    m_ePassiveSkillTargetType: EPassiveSkillTargetType
    m_iArrValues: list[int]
    m_szDescription: str
    m_szValueWithUnit: str

    def toJSON(self) -> str:
        return json.dumps({
            "PassiveSkillType": self.m_ePassiveSkillType.value,
            "PassiveSkillTargetType": self.m_ePassiveSkillTargetType.value,
            "Values": self.m_iArrValues,
            "Description": self.m_szDescription,
            "ValueWithUnit": self.m_szValueWithUnit
        })