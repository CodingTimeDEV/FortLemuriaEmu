# Endpoint: `/api/boot/top`

* **Status:** 🟡 Mock / Skeleton
* **Category:** <!-- e.g., Auth, Prologue, Home Farm / Lobby, Monsters, Combat -->
* **Related Game Classes (Cpp2IL):** Req: BootTopRequest ; Resp: BootTopResponse

---

## 📋 Overview
The primary "boot handshake" endpoint. Called early in the launch sequence to (1) synchronise the client clock with the server, (2) confirm the fixed-data (static game data: item tables, monster stats, UI strings, etc.) version the server expects, and (3) provide the list of per-type fixed-data hashes so the client can verify or download the correct static asset bundles before entering the lobby.


---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
"Accept": "application/msgpack", 
"Accept-Encoding": "gzip", 
"User-Agent": "[...]", 
"User-Token": "mocktoken1234567890", 
"lang": "1", 
"Host": "127.0.0.1:8092", 
"Connection": "Keep-Alive, TE", 
"TE": "identity"
```

### Payload Structure
```json
null
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |

---

## 📤 Response (Server ➔ Client)

### Expected JSON Structure
```json
{
  "serverTime": 1700000000,
  "fixedDataVersion": 1,
  "fixedDataHashList": [
    {
        "type": 1,
        "hash": ""
    }
  ]
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `serverTime` | `DateTime/int` | Current unix server time |
| `fixedDataVersion` | `int` | Integer version of the static data set. `1` in current mock impl. |
| `fixedDataHashList` | `array<FixedDataHashModel>` | One entry per fixed-data type the client must validate |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Returns a live `now()` timestamp but hardcoded `fixedDataVersion = 1` and placeholder hashes (`"h1"`, `"h3"`, …). Currently responds with `typeId`s `1, 3, 9, 19, 20, 21, 22, 23, 24, 26, 28, 29`
* **Client Dependencies / Edge Cases:** If `serverTime` is missing, the client throws a `NullReferenceException` and freezes on the loading screen (common pattern in C# boot flows).
If a type is present in the client's expected list but absent from `fixedDataHashList`, the client will attempt to hash the local file and fail the integrity check → full re-download or crash.
If `fixedDataVersion` is lower than the client's cached version, the client may still proceed (forward-compat) or reject the connection.
* **Database Requirements:** For the sake of this project a static implementation is probably sufficient.
