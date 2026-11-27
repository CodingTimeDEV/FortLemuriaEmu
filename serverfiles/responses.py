"""Shared response builders used across multiple routes."""
from typing import Any

import msgpack
from .config import (
    SKIP_PROLOGUE,
    MOCK_CHARACTER_ID,
    MOCK_CUR_QUEST,
    KEEP_FILE,
)
from . import skel
from .users import cur, uid, uname, update_user
from .utils import now

from serverfiles.types.classes.CCharacterModel import CCharacterModel
from serverfiles.types.classes.CCharacterProfileModel import CCharacterProfileModel

from serverfiles.types.enums.EGender import EGender
from serverfiles.types.enums.ECharacterBodyShape import ECharacterBodyShape

def mock_user_flags() -> list:
    return (
        [{"userId": uid(), "userFlagId": "1", "type": 7, "value": True}]
        if SKIP_PROLOGUE
        else []
    )


def account_response(model: str) -> dict:
    d = skel.default(model)
    d["serverTime"] = msgpack.Timestamp(seconds=now())
    U = uid()
    d["userConstant"].update(userId=U, userHash="mockhash")
    d["userSetting"].update(userId=U, isBirthday=True, enableCommunication=True)
    d["snsInfo"].update(userId=U, isRegisteredSteamAccount=cur()["snsSteam"])
    ua = d["userDataSet"]["userAttribute"]
    ua.update(
        userId=U,
        userAttributeId=U,
        name=uname(),
        personalCode=cur()["personalCode"],
    )

    isInQuest = MOCK_CUR_QUEST != -1
    if(isInQuest):
        d["userDataSet"]["userCurrentQuest"].update(
            userId=U,
            questId=MOCK_CUR_QUEST
        )
    else:
        d["userDataSet"]["userCurrentQuest"].update(
            userId=U
        )
        

    d["userDataSet"]["userFlags"] = mock_user_flags()
    ua["currentPartyNo"] = 1
    d["userDataSet"]["userPartyDataSet"]["userParties"] = [
        {"no": 1, "userId": U, "userPartyId": U, "name": uname()}
    ]
    d["userDataSet"]["userGeneralItemDataSet"]["currentGold"].update(
        userId=U, gold=0, paidGold=0, freeGold=0
    )
    d["userDataSet"]["userGeneralItemDataSet"]["userCharacters"] = [
        {
            "userId": U,
            "userCharacterId": "1",
            "playableCharacterId": 1,
            "level": 1,
            "hp": 100,
            "sp": 100,
            "attack": 10,
            "physicalDefense": 10,
            "magicalDefense": 10,
            "elementalPoint": 0,
            "playerSkillLevel": 1,
        }
    ]
    d["userDataSet"]["userPartyDataSet"]["userPartyUnits"] = [
        {
            "userId": U,
            "userPartyUnitId": "1",
            "userPartyId": U,
            "no": 1,
            "userCharacterId": "1",
            "userWeaponId": "1",
            "leftUserOptionMonsterId": "",
            "rightUserOptionMonsterId": "",
            "userAccessory1Id": "",
            "userAccessory2Id": "",
            "uniquePlayerId": 1,
            "playerSkillSlots": [],
        }
    ]
    uw = skel.default("UserWeaponModel")
    uw.update(
        userId=U,
        userWeaponId="1",
        weaponId=1,
        level=1,
        attack=10,
        elementalPoint=0,
        minAttack=10,
        maxAttack=10,
    )
    uw["obtainedAt"] = msgpack.Timestamp(seconds=now())
    d["userDataSet"]["userGeneralItemDataSet"]["userWeapons"] = [uw]

    # keep.txt filtering (only include top-level keys listed there)
    try:
        keep = open(KEEP_FILE).read().split()
        d = {k: v for k, v in d.items() if k in keep}
    except OSError:
        pass

    farm_data = skel.default("FarmDataSetModel")
    farm_data["updateIntervalSeconds"] = 60
    d["bootMasterDataSet"] = {
        "defaultTips": [{"id": 1, "title": "mocking", "image": "", "text": "mocking"}],
        "farmDataSet": farm_data,
    }
    return d


def ensure_registered() -> None:
    """Auto-register unknown accounts (mimics original reg_info side-effect)."""
    if not cur()["registered"] and cur()["steamId"] != "0":
        from . import users
        users.set_current_user(
            update_user(
                cur()["steamId"],
                registered=True,
                snsSteam=True,
                name=cur()["name"] or "Player%s" % cur()["userId"],
            )
        )


def mock_character() -> CCharacterModel:
    CharacterModel: CCharacterModel = CCharacterModel()
    CharacterModel.m_iCharacterId = MOCK_CHARACTER_ID
    CharacterModel.m_szName = "Mock"
    CharacterModel.m_szAnotherName = ""
    CharacterModel.m_szMkName = ""
    CharacterModel.m_iCharacterProfileId = 1
    CharacterModel.m_iModelId = 15
    CharacterModel.m_iSeqId = 0
    CharacterModel.m_szMotionListAssetName = "h_025001_uniq_m"
    CharacterModel.m_iIconId = 0
    CharacterModel.m_iDefaultWeaponId = 1
    CharacterModel.m_bIsPlayable = True

    return CharacterModel

def mock_character_profile() -> CCharacterProfileModel:
    CharacterProfileModel: CCharacterProfileModel = CCharacterProfileModel()
    CharacterProfileModel.m_iCharacterProfileId = 1
    CharacterProfileModel.m_szName = "Mock"
    CharacterProfileModel.m_eGender = EGender.Other
    CharacterProfileModel.m_eBodyShape = ECharacterBodyShape.Middle
    CharacterProfileModel.m_szVoice = ""
    CharacterProfileModel.m_iPersonality = 0
    CharacterProfileModel.m_szAmmoName = ""

    return CharacterProfileModel
