# Endpoint: `[METHOD] /api/path/to/endpoint`

* **Status:** 🔴 Unimplemented | 🟡 Mock / Skeleton | 🟢 Fully Implemented
* **Category:** <!-- e.g., Auth, Prologue, Home Farm / Lobby, Monsters, Combat -->
* **Related Game Classes (Cpp2IL):** <!-- e.g., `Game.Network.UserApiRequest`, `HomeFarmManager` -->

---

## 📋 Overview
<!-- Briefly explain when the client calls this endpoint and what it is used for (e.g., "Called right after loading into the Home Farm to fetch spawned NPCs and daily rewards."). -->


---

## 📥 Request (Client ➔ Server)

### Headers (if special)
```http
Authorization: Bearer <session_token>
Content-Type: application/json
```

### Payload Structure
```json
{
  "user_id": 12345,
  "example_flag": true
}
```

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `user_id` | `int` | Yes | Unique player ID |
| `example_flag` | `bool` | No | Purpose of this parameter (or `Unknown`) |

---

## 📤 Response (Server ➔ Client)

### Expected JSON Structure
```json
{
  "status": 0,
  "server_time": 1700000000,
  "data": {
    "npc_list": []
  }
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `status` | `int` | `0` = Success (list error codes if known) |
| `server_time` | `int` | Current Unix timestamp |
| `data.npc_list` | `array` | List of NPC objects to spawn (see notes below) |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** <!-- e.g., Currently returns an empty `npc_list` in `serverFiles/...` -->
* **Client Dependencies / Edge Cases:** <!-- e.g., "If `server_time` is missing, the client throws a NullReferenceException and freezes on the loading screen." -->
* **Database Requirements:** <!-- e.g., "Needs a `player_progress` table to persist prologue completion." -->
