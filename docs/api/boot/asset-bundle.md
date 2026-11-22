# Endpoint: `/api/boot/asset-bundle`

* **Status:** 🟡 Mock / Skeleton
* **Category:** Boot
* **Related Game Classes (Cpp2IL):** Req: BootAssetBundleRequest ; Resp: BootAssetBundleResponse

---

## 📋 Overview
Called during boot so the client can determine whether its local asset-bundle cache is up-to-date. The client compares the returned hash against the hash of its local bundle file; on mismatch it might trigger a download/patch of the new bundle.

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
  "assetBundleLatestHash": "00000000000000000000000000000000"
}
```

| Field | Type | Description / Expected Values |
| :--- | :--- | :--- |
| `assetBundleLatestHash` | `string` | 32-char hex string (MD5). Currently all zeros – a sentinel meaning "no update available". |

---

## 🧠 Reverse Engineering & Implementation Notes
* **Current Mock Behavior:** Returns a fixed 32-zero hash. The client will compare this to its local bundle hash; because it will almost never match the real production hash, the client may attempt a download and fail (or skip, depending on error handling).
* **Client Dependencies / Edge Cases:** If the hash string is not exactly 32 hex characters the client may throw a `FormatException`. The client likely hashes the current asset bundle on startup and only re-downloads on mismatch.
* **Database Requirements:** For the sakes of this project it's currently not required.
