# Endpoint: `POST /api/monster-index/mount-monster`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Monsters (Monster Index, Mount Monsters)
* **Related Game Classes (Cpp2IL):** `Ammo.MonsterIndexMountMonsterApi`, `Ammo.MonsterIndexMountMonsterRequest`, `Ammo.MonsterIndexMountMonsterResponse`, `Ammo.MountMonsterThumbnailModel`, `Ammo.MonsterThumbnailModel`, `Ammo.MonsterDictionaryTopScene` (`<OpenMountMonsterList>d__10`), `Ammo.MonsterDictionaryMonsterSelectSceneBase<T>`, `Ammo.MonsterDictionaryMonsterSelectViewModel`

---

## 📋 Overview
Called when the player opens the "Mount Monster" section of the monster index. The response lists all index entries as thumbnails. The client paginates locally (24 entries per page, `ElementsPerPage = 24`) and sorts and filters on its own. The models implement `IHasRarity`, `IHasElementalType`, `IHasMountType`, `IHasGrade` and `IHasMonsterIndexStatus` for this.

The HTTP method: the API constructor sets a method field of `2`, which I read as POST based on the pattern across all 220 `*Api` classes. The constructor also sets two flag bytes (`257`); their meaning is unknown.

---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
Accept: application/msgpack
Accept-Encoding: gzip
Authorization: Bearer <auth_token>
```

### Payload Structure
No body. `MonsterIndexMountMonsterRequest` has no fields.

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| – | – | – | – |

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
  "thumbnails": [
    {
      "indexNo": 1,
      "mountMonsterId": 1000001,
      "rarity": 1,
      "elementalType": 1,
      "mountType": 1,
      "grade": 1,
      "monsterThumbnail": {
        "monsterId": 1000001,
        "name": "Test",
        "iconId": 1000001,
        "monsterIndexStatus": 4,
        "monsterModelId": 1000001
      }
    }
  ]
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `thumbnails` | array | `MountMonsterThumbnailModel[]`, one entry per index slot |
| `thumbnails[].indexNo` | `int` | Index number, shown as text (`Int32.ToString`) |
| `thumbnails[].mountMonsterId` | `long` | ID used later for `mount-monster-detail` |
| `thumbnails[].rarity` | `int` | `Rarity` 0–8 (`Star0` … `Star8`) |
| `thumbnails[].elementalType` | `int` | 0 None, 1 Fire, 2 Wind, 3 Thunder, 4 Water, 5 Light, 6 Dark |
| `thumbnails[].mountType` | `int` | 0 None, 1 Strike, 2 Power, 3 Wide, 4 HeavyMagic, 5 RapidMagic |
| `thumbnails[].grade` | `int` | Grade |
| `thumbnails[].monsterThumbnail` | object | `MonsterThumbnailModel` |
| `…monsterThumbnail.monsterId` | `int` | Monster ID |
| `…monsterThumbnail.name` | `string` | Display name |
| `…monsterThumbnail.iconId` | `int` | Icon asset `ui/monster/icon/m_{iconId:D7}` (the bundle must exist locally) |
| `…monsterThumbnail.monsterIndexStatus` | `int` | 0 Unidentified, 1 NewIdentified, 2 Identified, 3 NewObtained, 4 Obtained. `Unidentified` is probalbly shown as a silhouette |
| `…monsterThumbnail.monsterModelId` | `int` | Model ID) |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Returns one entry with `iconId: 1000001` (the list loads).
* **Client Dependencies / Edge Cases:**
  * An `iconId` without a local bundle leads to "Failed to load. Return to title screen" and, in `Player.log`, to `Unable to open archive file …/StreamingAssets/1/w/…` (observed; `1000001` works).
  * The response and `MountMonsterThumbnailModel` both have `UpdateDatabase()`, so entries end up in the client database. `mountMonsterId` should be unique.
  * An entry that is not in `thumbnails` does not appear in the game. I did not test how the client copes with very large lists.
  * HTTP `404` shows a connection-error dialog and the game keeps running; HTTP `200` with an empty or incomplete body freezes the game without a crash.
* **Database Requirements:** A master table of mount monsters (ordered by `indexNo`) and, per player, the index status (`monsterIndexStatus`). This is a recommendation.