"""Handlers for /api/data/load (the large switch on Type=N)."""
from .. import skel
from ..config import MOCK_CHARACTER_ID
from ..responses import mock_character, mock_character_profile
from . import register


def _data_load(q, b):
    d = skel.default("DataLoadResponse")
    s = d["dataSet"]

    if "type=9" in q or "Type=9" in q or q.startswith("9"):
        pc = skel.default("PlayableCharacterModel")
        pc.update(
            playableCharacterId=1,
            characterId=MOCK_CHARACTER_ID,
            rarity=1,
            mountType=1,
            playerSkillId=1,
            extremeSkillId=1,
            hateId=1,
            defaultPlayerSkillLevel=1,
            minHp=100, midHp=100, maxHp=100,
            minSp=100, midSp=100, maxSp=100,
            minAttack=10, midAttack=10, maxAttack=10,
        )
        s["playableCharacters"] = [pc]

    elif "type=20" in q or "Type=20" in q:
        s["characters"] = [mock_character()]

    elif "Type=1&" in q:
        w = skel.default("WeaponModel")
        w.update(weaponId=1, name="Mock", rarity=1, weaponType=1, modelId=220002, use=1)
        s["weapons"] = [w]

    elif "Type=3&" in q:
        mm = skel.default("MountMonsterModel")
        mm.update(
            mountMonsterId=1, name="Mock", monsterId=1, rarity=1,
            mountType=1, sequenceId=1, grade=1, isDefault=True,
            hateId=1, playerSkill1Id=1,
            baseHp=100, baseSp=100, baseAttack=10,
            basePhysicalDefense=10, baseMagicalDefense=10,
        )
        s["mountMonsters"] = [mm]

    elif "Type=19&" in q:
        mo = skel.default("MonsterModel")
        mo.update(monsterId=1, name="Mock", modelId=1026002, sequenceId=1)
        s["monsters"] = [mo]

    elif "Type=22&" in q:
        ps = skel.default("PlayerSkillModel")
        ps.update(playerSkillId=1, name="Mock", mountType=1)
        sts = skel.default("PlayerSkillStatusModel")
        sts.update(
            playerSkillStatusId=1, playerSkillId=1, rank=1,
            attackId=201, consumedSp=0, recoveredSp=0,
            wincePoint=0, omegaDrivePoint=0, omegaDrivePointByWeakPoint=0,
        )
        ps["statuses"] = [sts]
        s["playerSkills"] = [ps]

    elif "Type=23&" in q:
        pt = skel.default("PlayerTapSkillModel")
        pt.update(playerTapSkillId=1, playerSkillId=1, mountType=1, no=1)
        s["playerTapSkills"] = [pt]

    elif "Type=24&" in q:
        st = skel.default("PlayerStepSkillModel")
        st.update(playerStepSkillId=1, mountType=1, type=1, playerSkillId=1)
        s["playerStepSkills"] = [st]

    elif "Type=28&" in q:
        h = skel.default("HateModel")
        h.update(hateId=1, description="Mock", basePoint=100)
        s["hates"] = [h]

    elif "Type=26&" in q:
        s["passiveSkills"] = []

    elif "Type=21&" in q:
        s["characterProfiles"] = [mock_character_profile()]

    elif "Type=29&" in q:
        s["bullets"] = []

    return d


register("/api/data/load", _data_load)
