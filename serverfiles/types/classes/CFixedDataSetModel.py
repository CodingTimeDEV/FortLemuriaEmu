from typing import Any

from serverfiles.types.classes.CTypeImplBaseClass import CTypeImplBaseClass
from serverfiles.types.classes.CWeaponModel import CWeaponModel
from serverfiles.types.classes.CAccessoryModel import CAccessoryModel
from serverfiles.types.classes.CMountMonsterModel import CMountMonsterModel
from serverfiles.types.classes.COptionMonsterModel import COptionMonsterModel
from serverfiles.types.classes.CMaterialModel import CMaterialModel
from serverfiles.types.classes.CUtilityTicketModel import CUtilityTicketModel
from serverfiles.types.classes.CPlayableCharacterModel import CPlayableCharacterModel
from serverfiles.types.classes.CStampModel import CStampModel
from serverfiles.types.classes.CQuestOnlyItemModel import CQuestOnlyItemModel
from serverfiles.types.classes.CEmblemModel import CEmblemModel
from serverfiles.types.classes.CMountMonsterEggModel import CMountMonsterEggModel
from serverfiles.types.classes.CFarmBuildingModel import CFarmBuildingModel
from serverfiles.types.classes.CItemRecipeModel import CItemRecipeModel
from serverfiles.types.classes.CMonsterModel import CMonsterModel
from serverfiles.types.classes.CCharacterModel import CCharacterModel
from serverfiles.types.classes.CCharacterProfileModel import CCharacterProfileModel
from serverfiles.types.classes.CPlayerSkillModel import CPlayerSkillModel
from serverfiles.types.classes.CPlayerTapSkillModel import CPlayerTapSkillModel
from serverfiles.types.classes.CPlayerStepSkillModel import CPlayerStepSkillModel
from serverfiles.types.classes.COptionMonsterSkillModel import COptionMonsterSkillModel
from serverfiles.types.classes.CPassiveSkillModel import CPassiveSkillModel
from serverfiles.types.classes.CFarmBuildingUpgradeModel import CFarmBuildingUpgradeModel
from serverfiles.types.classes.CHateModel import CHateModel
from serverfiles.types.classes.CBulletModel import CBulletModel
from serverfiles.types.classes.CMasterPartialDataModel import CMasterPartialDataModel

class CFixedDataSetModel(CTypeImplBaseClass):
    m_arrWeapons: list[CWeaponModel]
    m_arrAccessoryModel: list[CAccessoryModel]
    m_arrMountMonsterModel: list[CMountMonsterModel]
    m_arrOptionsMonsterModel: list[COptionMonsterModel]
    m_arrMaterialModel: list[CMaterialModel]
    m_arrUtilityTickets: list[CUtilityTicketModel]
    m_arrPlayableCharacterModel: list[CPlayableCharacterModel]
    m_arrStampModel: list[CStampModel]
    m_arrQuestOnlyItemModel: list[CQuestOnlyItemModel]
    m_arrEmblemModel: list[CEmblemModel]
    m_arrMountMonsterEggModel: list[CMountMonsterEggModel]
    m_arrFarmBuildingModel: list[CFarmBuildingModel]
    m_arrItemRecipeModel: list[CItemRecipeModel]
    m_arrMonsterModel: list[CMonsterModel]
    m_arrCharacterModel: list[CCharacterModel]
    m_arrCharacterProfileModel: list[CCharacterProfileModel]
    m_arrPlayerSkillModel: list[CPlayerSkillModel]
    m_arrPlayerTapSkillModel: list[CPlayerTapSkillModel]
    m_arrPlayerStepSkillModel: list[CPlayerStepSkillModel]
    m_arrOptionMonsterSkillModel: list[COptionMonsterSkillModel]
    m_arrPassiveSkillModel: list[CPassiveSkillModel]
    m_arrFarmBuildingUpgradeModel: list[CFarmBuildingUpgradeModel]
    m_arrHateModel: list[CHateModel]
    m_arrBulletModel: list[CBulletModel]
    m_arrMasterPartialDataModel: list[CMasterPartialDataModel]

    def toJSON(self) -> dict[str, Any]:
        return {
            "weapons": [weapon.toJSON() for weapon in self.m_arrWeapons],
            "accessories": [accessory.toJSON() for accessory in self.m_arrAccessoryModel],
            "mountMonsters": [mount.toJSON() for mount in self.m_arrMountMonsterModel],
            "optionMonsters": [option.toJSON() for option in self.m_arrOptionsMonsterModel],
            "materials": [material.toJSON() for material in self.m_arrMaterialModel],
            "utilityTickets": [ticket.toJSON() for ticket in self.m_arrUtilityTickets],
            "playableCharacters": [character.toJSON() for character in self.m_arrPlayableCharacterModel],
            "stamps": [stamp.toJSON() for stamp in self.m_arrStampModel],
            "questOnlyItems": [item.toJSON() for item in self.m_arrQuestOnlyItemModel],
            "emblems": [emblem.toJSON() for emblem in self.m_arrEmblemModel],
            "mountMonsterEggs": [egg.toJSON() for egg in self.m_arrMountMonsterEggModel],
            "farmBuildings": [building.toJSON() for building in self.m_arrFarmBuildingModel],
            "itemRecipes": [recipe.toJSON() for recipe in self.m_arrItemRecipeModel],
            "monsters": [monster.toJSON() for monster in self.m_arrMonsterModel],
            "characters": [character.toJSON() for character in self.m_arrCharacterModel],
            "characterProfiles": [profile.toJSON() for profile in self.m_arrCharacterProfileModel],
            "playerSkills": [skill.toJSON() for skill in self.m_arrPlayerSkillModel],
            "playerTapSkills": [skill.toJSON() for skill in self.m_arrPlayerTapSkillModel],
            "playerStepSkills": [skill.toJSON() for skill in self.m_arrPlayerStepSkillModel],
            "optionMonsterSkills": [skill.toJSON() for skill in self.m_arrOptionMonsterSkillModel],
            "passiveSkills": [skill.toJSON() for skill in self.m_arrPassiveSkillModel],
            "farmBuildingUpgrades": [upgrade.toJSON() for upgrade in self.m_arrFarmBuildingUpgradeModel],
            "hates": [hate.toJSON() for hate in self.m_arrHateModel],
            "bullets": [bullet.toJSON() for bullet in self.m_arrBulletModel],
            "masterPartialData": [data.toJSON() for data in self.m_arrMasterPartialDataModel]
        }
