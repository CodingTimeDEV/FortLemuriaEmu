# Endpoint: `POST /api/monster-index/option-monster-detail`

* **Status:** 🟡 Mock / Skeleton (the detail view does not load yet, see notes)
* **Category:** Monsters (Monster Index, Option Monster Detail)
* **Related Game Classes (Cpp2IL):** `Ammo.MonsterIndexOptionMonsterDetailApi`, `Ammo.MonsterIndexOptionMonsterDetailRequest`, `Ammo.MonsterIndexOptionMonsterDetailResponse`, `Ammo.OptionMonsterModel` (getter `Monster`), `Ammo.MonsterModel`, `Ammo.OptionMonsterSkillModel`, `Ammo.MonsterDictionaryOptionMonsterDetailScene`, `Ammo.MonsterDictionarySceneController`, `Ammo.OptionMonsterBuildParam`, `Ammo.MonsterBuildParam`, `Ammo.CharacterBuilder` (`SimpleMonster`), `Ammo.CharacterBuildAssetExtensions` (`MonsterPrefab`, `MonsterCommonSequence`)

---

## 📋 Overview
Called when an entry of the option monster list is opened. The response contains the option monster's master data, the matching `MonsterModel`, drop quests, a description and the option skill. The client builds the 3D model from it (`MonsterDictionarySceneController.Setup(OptionMonsterModel, isSilhouette)`).

The HTTP method: the API constructor sets a method field of `2`, which I read as POST based on the pattern across all 220 `*Api` classes. The constructor also sets a flag byte of `1`; its meaning is unknown.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
Accept: application/msgpack
Accept-Encoding: gzip
Authorization: Bearer <auth_token>
```

### Payload Structure
```json
{ "optionMonsterId": 101001610 }
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `optionMonsterId` | `long` | Yes | `optionMonsterId` from the list response |

---

## 📤 Response (Server ➔ Client)

### Response Headers
```http
Content-Type: application/msgpack
```

### Expected Structure (MessagePack map, shown as JSON)
```json
{
  "commonResource": { "subNotifications": [], "badges": [] },
  "optionMonster": {
    "optionMonsterId": 101001610, "name": "Test", "indexNo": 1,
    "monsterId": 101001610, "iconId": 101001610, "rarity": 1,
    "radius": 1.0, "scaleFactor": 1.0, "role": 1,
    "price": 0, "baseAttack": 0, "elementalType": 1, "baseElementalPoint": 0,
    "baseEvaluation": 0, "optionMonsterSkillId": 1, "hateId": 0,
    "optionMonsterAi": {
      "optionMonsterAiId": 1, "aiId": 0, "battleRange": 0,
      "searchRange": 0, "personalSpace": 0, "fieldOfView": 0
    }
  },
  "monster": {
    "monsterId": 101001610, "name": "Test", "evolutionStep": 1, "blowRate": 0,
    "category": 0, "species": 1, "voiceCategory": 0,
    "modelId": 101001610, "motionId": 202000110, "sequenceId": 202000110
  },
  "dropQuests": [],
  "description": { "text": "Test", "iconType": 1, "isLocked": false },
  "optionMonsterSkill": {
    "optionMonsterSkillId": 1, "name": "Test", "description": "Test",
    "attackType": 1, "range": 0, "statuses": [],
    "wincePoint": 0, "elementalType1": 1, "elementalType2": 0, "elementalType3": 0,
    "attackId": 0, "attackActionIds": [], "additionalEffectIds": [],
    "bulletIds": [], "noVanishmentAttackIds": [],
    "baseMaxCharge": 0, "baseBreakPoint": 0, "baseAttackPower": 0,
    "baseElementalPower1": 0, "baseElementalPower2": 0, "baseElementalPower3": 0,
    "baseCoolTime": 0, "additionalEffectBaseValues": [], "additionalEffectBaseDurations": [],
    "baseVanishWaitTime": 0.0
  }
}
```
`202000110` for `motionId` / `sequenceId` is only an **untested** placeholder. All three of its bundles (`seq_list`, `motion_list`, `transition_list`) exist in the asset manifest (see notes).

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `optionMonster` | object | `OptionMonsterModel`, fields below |
| `monster` | object | `MonsterModel` (same fields as in `mount-monster-detail`). The client finds it through `optionMonster.monsterId` in its database (see notes) |
| `dropQuests` | array | `ModifiedQuestModel[]`; `[]` is enough for a mock |
| `description` | object | **A single** `MonsterDescriptionModel` (`text`, `iconType`, `isLocked`), not an array |
| `optionMonsterSkill` | object | `OptionMonsterSkillModel`, fields below |

**`OptionMonsterModel`**

| Field | Type | Description |
| :--- | :--- | :--- |
| `optionMonsterId` | `long` | ID |
| `name` | `string` | Display name |
| `indexNo` | `int` | Index number |
| `monsterId` | `int` | Key for the `MonsterModel` lookup (not `0`, unique, identical to `monster.monsterId`) |
| `iconId` | `int` | Icon asset |
| `rarity` | `int` | 0–8 |
| `radius`, `scaleFactor` | `float` | Size and scale (`0` makes the model invisible, and triggers a background client error) |
| `role` | `int` | 1 Attacker, 2 Tanker, 3 Healer, 4 Buffer, 5 Debuffer |
| `price`, `baseAttack`, `baseElementalPoint`, `baseEvaluation`, `hateId` | `int` | Values |
| `elementalType` | `int` | 0–6 |
| `optionMonsterSkillId` | `long` | Reference to `optionMonsterSkill.optionMonsterSkillId` |
| `optionMonsterAi` | object | `OptionMonsterAiModel`: `optionMonsterAiId` (long), `aiId`, `battleRange`, `searchRange`, `personalSpace`, `fieldOfView` (all int) |

**`OptionMonsterSkillModel`**

| Field | Type | Description |
| :--- | :--- | :--- |
| `optionMonsterSkillId` | `long` | ID |
| `name`, `description` | `string` | Display texts |
| `attackType` | `int` | 0 None, 1 PhysicalAttack, 2 MagicalAttack |
| `range` | `int` | Range |
| `statuses` | array | `OptionMonsterSkillStatusModel[]`. Per entry: `skillId` (long), `limitBreakStep` (int), `additionalEffectValues` (int[]), `maxCharge`, `coolTime`, `attackPower`, `elementalPower1`, `elementalPower2`, `elementalPower3`, `breakPoint` (int), `vanishWaitTime` (float), `additionalEffectDurations` (int[]). How many steps the UI expects is unknown |
| `wincePoint` | `int` | Unknown |
| `elementalType1`, `elementalType2`, `elementalType3` | `int` | 0–6 |
| `attackId` | `int` | Unknown |
| `attackActionIds`, `additionalEffectIds`, `bulletIds`, `noVanishmentAttackIds`, `additionalEffectBaseValues`, `additionalEffectBaseDurations` | `int[]` | `[]` in the mock |
| `baseMaxCharge`, `baseBreakPoint`, `baseAttackPower`, `baseElementalPower1`, `baseElementalPower2`, `baseElementalPower3`, `baseCoolTime` | `int` | Base values |
| `baseVanishWaitTime` | `float` | Base value |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** All fields set. The response is accepted, but the view still aborts with "Failed to load" because three bundles are missing (see below).
* **Client Dependencies / Edge Cases:**
  * **Lookup through the database:** `OptionMonsterModel.Monster` is a getter that searches the client database for `MonsterId == optionMonster.monsterId`. The `monster` object of the response ends up there via `UpdateDatabase()`. Use a unique `monsterId` other than `0`, and restart the game after changing IDs.
  * **Which bundles are loaded (from `CharacterBuilder.SimpleMonster`, 🔎):**

    | Field | Bundle name |
    | :--- | :--- |
    | `monster.modelId` | `character/monster/model/m_{id:D7}` |
    | `monster.sequenceId` | `character/enemy/sequence/en_{id:D6}_seq_list` |
    | `monster.motionId` | `character/enemy/animation/en_{id:D6}_motion_list` and `…_transition_list` |
    | pattern texture | `character/monster/patterntexture/m_ptn_{name}` (no error so far) |

    `D6` is only the minimum width; the IDs are 7 or 9 digits long.
  * **Missing bundles:** If a bundle is not listed in the manifest `local_latest_custom_manifest`, `DefaultManifest.GetAssetBundleVersion` returns `name.GetHashCode()` instead of a Hash128 (read from the ISIL). That produces a numeric path such as `StreamingAssets/1/w/-6/13/123133`, while existing bundles live under hex paths such as `b2/be/d1cee40f…`. The client ignores `assetBundleLatestHash` from `boot/asset-bundle` and hard-codes the manifest name `local_latest_custom_manifest` (confirmed from the ISIL).
  * HTTP `404` shows a connection-error dialog and the game keeps running; HTTP `200` with an empty or invalid body freezes the game without a crash.
  * Invalid or non resolveable asset Ids force a "failed to load asset" error and failback to the main menu.
* **Open Problem:** The model `m_101001610` (and `…611` to `…614`) is listed in the manifest. However, the models of the families 101 to 104 have **no** sequence or motion list under their own ID there. Their real `sequenceId` and `motionId` most likely point to the lists of another monster (inferred from the absence). Which ones is stored in the master data (`MonsterModel`: `ModelId`, `MotionId`, `SequenceId`), not in the manifest. For testing, used random IDs for which `seq_list`, `motion_list` and `transition_list` exist. The loading errors then disappear, but the animation will probably not fit the model (unknown original values).
* **Database Requirements:** Master data per option monster including the `MonsterModel` mapping (`ModelId` / `MotionId` / `SequenceId`) and a skill table with steps.