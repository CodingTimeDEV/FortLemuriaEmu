# Volzerk (AMMO) – Boot Process and Server Response

Sources: Cpp2IL (diffable-cs / isil) + il2cpp.json from `ida-proj`. Function bodies are only available as assembly/ISIL, not as C#.
Everything marked "(presumed)" is derived from assembly and has not been tested.

## Hosts (Ammo.NetworkSettings / NetworkHosts)
| Field | Value |
|---|---|
| Protocol | `https` |
| apiHost | `ammo.colopl.jp` |
| assetHost | `static.ammo.colopl.jp/release` |
| toolHost | `tool.ammo.colopl.jp` |
| LOCAL_* constants (unused) | `http://localhost:8092` |

`NetworkSettings.GetHosts()` always returns the production values (`NetworkHostType` only has `None`/`Prod`).

URL patterns:
- `GetBaseUrl()` = `{protocol}://{apiHost}` = **`https://ammo.colopl.jp`** (all normal API calls)
- `GetProductionFixedDataBaseUrl()` = `{protocol}://api.{apiHost}` = `https://api.ammo.colopl.jp` (Fixed/Master Data, `/api/data/load`)
- `GetRawAssetBaseUrl()` = `https://static.ammo.colopl.jp/release/assets/streaming`
- `GetToolUrl()` = `https://tool.ammo.colopl.jp/tool`

## Boot Process
1. `BootScene.OnCreateSceneImpl` sets up text/plugins and creates `BootTopApi`.
2. `BootTopApi` is `Api<BootTopRequest, BootTopResponse>`:
   - **GET** (HTTPMethods 0), path `/api/boot/top`, no parameter body
   - `Authorize = false`, `IgnoreError = false`
   - Call is therefore: `GET https://ammo.colopl.jp/api/boot/top`
3. Response → `BootTopResponse`:
   - `ServerTime` (DateTime)
   - `FixedDataVersion` (int)
   - `FixedDataHashList` (array of `FixedDataHashModel { Type: FixedDataType, Hash: string }`)
4. Then `FixedDataLoader.Create` + `FixedDataLoader.Load(hashModel)` for each hash entry; all are awaited (`WaitForCompletion`).
   - Fixed Data request: `/api/data/load` with query, headers `Accept: application/msgpack`, `Accept-Encoding: gzip`, timeout 15 s, response `DataLoadResponse`.
   - If `FixedDataHashList` is empty, this step is skipped (presumed).
5. Then `BootScene.BootRequestCoroutine` (→ `/api/boot/registered-info` with `BootRegisteredInfoResponse`, Steam: `/api/boot/steam-app-country` with `Country`, `/api/boot/asset-bundle` with `AssetBundleLatestHash`, `/api/boot/app-age`) (order not verified).

## Transport / Response Format
- BestHTTP; success = HTTP status 200–299 or 304 (`ApiResponse.IsSuccess`).
- Body: **MessagePack** (`SouthPointe.Serialization.MessagePack`), content type presumably `application/msgpack`.
- Serializer configuration (`AmmoMsgPackFormatter.Create`):
  - Objects as **maps** with **camelCase** keys (`serverTime`, `fixedDataVersion`, `fixedDataHashList`; `type`, `hash`)
  - `DateTime` in **Epoch** mode (`DateTimePackingFormat = 2`; unit presumably seconds)
  - Enums: integer; unknown fields are ignored
  - Custom handler for `Colopl.SecureInt`
- Errors: status != 2xx is read via `ErrorSerializer` as `ApiError { Message, Code, Type, File, Line, Trace }`. 422, 429 (`Retry-After`), and 502 are handled separately (retry). 401 and code 1000 trigger dialogs (`NetworkManager.ErrorHandling`).
- Headers: request `Authorization: Bearer <token>`, `user-token`, `AssetBundle-Manifest`, `Retry-Count`; response: `authorization` (adopted as AccessToken), `user-token`, `x-server-time`.

## Minimal Response for `/api/boot/top` (Hypothesis)
HTTP 200 Content-Type: application/msgpack Body (msgpack map): { "serverTime": <epoch>, "fixedDataVersion": <int>, "fixedDataHashList": [] }

Whether the game starts with this and no master data is untested. It will most likely break at the latest on the Fixed Data tables. The hashes refer to data that a mock server would have to provide.

## Open Questions
- Redirecting to a custom server: hosts are hardcoded. Additionally, an `SslVerifyer` is set when using `https`. So a hosts file entry + own certificate, or a patch of `NetworkSettings.GetHosts` is needed (target function `0x180603C60` is the `NetworkHosts` constructor; the strings are passed by pointer in code).
- Further checks after boot (version/maintenance, `/api/ntc/check`, `/api/time/top`) not investigated.

## Practical Test (Mock Server, Verified)
Test copy test\volzerk with patched global-metadata.dat (hosts → 127.0.0.1:8092, https literal → http) and patched GameAssembly.dll (SslVerifyer.IsValid → `mov al,1; ret`). Despite the literal patch, the game still speaks TLS, so test\mock_server.py responds on port 8092 with TLS (self-signed) and plaintext.

Observed requests:
1. GET /api/boot/asset-bundle → {assetBundleLatestHash: "<hash>"}
2. GET /api/boot/top → {serverTime, fixedDataVersion: 1, fixedDataHashList: []}
3. GET /api/boot/steam-app-country?ticket=... → {country: "JP"} (untested)

With 1 and 2, the game reaches the title screen ("GAME START", version 1.3.1). Request headers: Accept: application/msgpack, lang: 1. Error responses (404 + {message, code, type}) are shown by the game as a "Communication Error" dialog with the message text.

## Practical Test Part 2 (as of 17.10.2026)
Additional patches in test\volzerk\GameAssembly.dll:
- `WaitGetAuthSessionTicket`: conditional jump `75` → `EB` (file offset 0x46911d), otherwise boot hangs on the Steam ticket.
- `StartupSequence.ConsentForm` (VA 0x18050aeea): directly calls `ConsentForm_b__0(true)`, bypassing the consent dialog.

Mock responses (all MessagePack, camelCase maps):
- GET  /api/boot/steam-app-country → {country: 0}   (0 = Global, English dialog; JP = Japanese)
- POST /api/boot/app-age           → {age: 2}
- POST /api/sns/login-*            → {} with HTTP 200
- POST /api/tip/list               → {tips: [{id, title, image, text}]}
- POST /api/boot/registered-info   → BootRegisteredInfoResponse (request {steamClient: true}); skeleton from C# stubs (test\skel.py)

Authentication:
- AccessToken comes from the response header `Authorization: Bearer <token>` (exactly this casing; lowercase does not work). `NetworkManager.IsAuthenticated` = AccessToken not empty.
- `user-token` (response header) is adopted as `UserAuth.UserToken`. The game sends both headers back on every subsequent request.
- With a stored token, BootScene calls `registered-info` directly at startup (before GAME START).
- If `UserManager.HasMy` is false, the game shows "Invalid account, reset?" (`GameManager.IsInvalidAuthToken`).

Language:
- Stored in PlayerPrefs (`SaveData.Key.Language` = 28, registry HKCU\Software\colopl\Volzerk, names hashed). 0 = Japanese, 1 = English.
- `BootScene.OnCreateSceneImpl` only sets the value if it is missing (−1): Steam UI language "japanese" → Japanese, otherwise English. The request header `lang` corresponds to the value.
- A previously stored value of 0 therefore persisted. Solution: delete PlayerPrefs values (backup: test\prefs_backup.reg). Then `lang: 1`.

Open:
- The full registered-info response (with bootMasterDataSet/generalItemDataSet) causes the game to hang on a black screen; the partial response (fields serverTime, userConstant, userSetting, snsInfo, message, clientConfigs, userDataSet) completes. Controlled via test\keep.txt (list of sent top-level fields).
- HasMy remains false (SetupUserData not yet verified).

## Practical Test Part 3 (as of 18.10.2026): Title → Home Map
Dump overview: see `dump_index.md`. Test routine: `test\test_run2.ps1` (fresh mock, 10 s, game, 5 s + wait, screenshot, end game; no clicking).

Cause of the hang after GAME START (loading tips):
- `UILoadingTips.Show` reads `Database.I.DefaultTips` = `BootMasterDataSetModel.DefaultTips`. If `bootMasterDataSet` is missing in `registered-info`, the callback is never triggered and `StartupScene.NextSceneRoutine` waits indefinitely.
- Solution: `registered-info` always includes `bootMasterDataSet = {defaultTips: [{id:1,title:'mocking',image:'',text:'mocking'}]}` (set after the `keep.txt` filter); `/api/tip/list` serves the same tip. The full skeleton of `bootMasterDataSet`/`generalItemDataSet` still leads to a black screen.
- Abandoned attempt: DLL patch `UILoadingTips.Show` → `SafeInvoke(cb)` (black screen; file `test\GameAssembly.with_tips.dll`, active DLL = `GameAssembly.before_tips.dll`).

Further steps in `NextSceneRoutine` (Frida-verified, hooks h13/h14):
1. `ShowLoading` → tips callback.
2. `SteamPaymentManager.SignInWithSteam` → `WaitGetAuthSessionTicket` → `POST /api/steam-payment/authenticate` (body `ticket`, response `SteamPaymentAuthenticateResponse {userSetting, termsOfService, isJp}`; mock: skeleton with `userSetting.userId='1'`).
3. `MyUser.CurrentQuest` (`Database.UserCurrentQuests` filtered by `userId`): if `userDataSet.userCurrentQuest.userId` is empty, it returns `null` and the coroutine silently exits. Mock sets `userId='1'`.
4. `MapTransitionInfo.CreateHome` → `GameSceneManager.Dispatch("ROOT_GOTO_IN_GAME")` → `InGameSetupSequence.CreateSingleHome` → `POST /api/farm/top` (`FarmTopResponse`, mock: skeleton + `userAttribute`).
5. Callback `CreateSingleHome.b__0` builds the sequence `InGameSinglePlayerSetup` → `InGameMapSetup(mapGenerateInfo)` → `InGameMapSetupPostProcess` → `InGameHomeSetupPostProcess`.

Current status: `InGameMapSetup.Process` (→ `MapManager.Initialize`) remains stuck in state 0, screen stays on loading tips, no error message. Suspect: empty `mapGenerateInfo` (Map ID/Seed 0) in the `FarmTopResponse` skeleton and/or missing asset bundles (`asset-bundle` only returns a dummy hash).

New/changed mock endpoints: `POST /api/steam-payment/authenticate`, `POST /api/farm/top`, `GET /api/tip/list`. Mock restart is unstable: `restart_mock.ps1` may need to be run twice.

### Practical Test Part 4 (Map Initialization, as of 18.10.2026)
- `MapManager.LoadMapScene(sceneId)` receives `mapGenerateInfo.map.mapId` (not `sceneId`). For `map.type=0` (MapType.None) or an unknown ID, the bundle `map/town/scene/<ID 11-digit>` is not found (`Unable to open archive file ...\1\w\18\97\579806` in `Player.log`).
- Valid town scenes are listed in `StreamingAssets\1\w\local_latest.manifest` (including `10010100102`, `10010120101`, `10100101101`, `10200101101`, `10019310101`). Mock now uses `map.mapId=10010100102`, `map.type=1` (Town). After that the bundles load, `LoadMapScene`/`Initialize76` run to completion, and `InGameMapSetup` finishes.
- Next blocker: `InGameSetupSequence._ProcessParallelSetup` waits on `InGameSinglePlayerSetup`. There, `MyUser.GetCurrentParty` returns null as long as no `UserPartyModel` with `no == userAttribute.currentPartyNo` exists (mock: `userParties=[{no:1,...}]`, `currentPartyNo=1`). After that, `CharacterManager.CreateHumanUnit` is called, but `HasCurrent` remains false: `userPartyUnits` with `userCharacterId` plus associated user character data are missing, and presumably master data (characters/weapons; `fixedDataHashList` is empty, `/api/data/*` not mocked).
- Note: Frida hook on the NRE thrower `0x1802954D0` (even without backtrace) causes a crash. `Player.log` (`%USERPROFILE%\AppData\LocalLow\colopl\Volzerk\Player.log`) shows bundle loading errors.
- Hook scripts: `h18`–`h26.js` in the session folder (Town NameData, LoadFromFile paths, Setup coroutines, CharacterManager).

### Practical Test Part 5 (Character Build, as of 18.10.2026)
- The mock was additionally serving `/api/data/load` at this point (types 1, 3, 9, 19, 20, 22, 23, 24), `characterId=15`, weapon `modelId=220002`, `MountType` Strike=1. The asset bundles observed at the time (sounds, effects, scenes, sequences) loaded; this does not imply that no further assets are missing. Later findings regarding the character image are in Part 11.
- Map scene (`MapManager.LoadMapScene`, `_LoadSceneAsync`) is loaded and active; scenes `Common`, `InGame`, then `Map/Town/Scene/10010100102`.
- `CharacterBuilder.Process` (MoveNext `0x180312370`) starts 5 child coroutines (`CharacterSequenceAsset.Execute` d6 ×3, d17, d10); all 5 complete. The runner itself is only called **11 times** (state 0 → 1, then 10× `yield null` returning true) and never again. `CreateUnit`, `_CreateUnit`, `AddPlayerUnit` are never reached, `HasCurrent` remains false, `InGameSinglePlayerSetup.Process` hangs in state 1.
- Ruled out (hooks h70–h75): the `CharacterManager` host (`this+0x28`) is not destroyed, its GameObject remains `activeInHierarchy` (checked up to frame ~1960), `CharacterManager.Update` continues to run. `MonoBehaviour.StopCoroutine*`/`StopAllCoroutines` are not called on the host (only on UI classes, `OnDisable` of text controllers). Scene switches (`LoadScene` Map, `SetActiveScene`) only occur after the stop, no `Unload`. No exception (no `RaiseException` during the runner).
- Open question: why Unity stops driving the runner after ~11 frames despite the host being active. Most likely: the coroutine was started via `StartCoroutine_Auto` on a different object/wrapper (caller backtrace: `181190bcc`, `180099e86`, `18025c299`) or a wrapper aborts it.
- Frida notes: `Module.getExportByName(null, ...)` does not exist (→ `Process.getModuleByName('KERNELBASE.dll')`). **Stalker on the game thread causes a crash** (do not use again). `Backtracer.ACCURATE` produces usable stacks.
- Hook scripts: `h52`–`h77.js` in the session folder (h70 counters/scenes, h71 d30 state, h72 StopCoroutine, h73 activeInHierarchy, h74 callers, h75 Enter/Leave, h76 RaiseException, h77 Stalker = crash).

## Practical Test Part 6 – Handover (as of 18.10.2026)

**Goal:** Game starts fully (main menu/home). Currently it hangs on the loading tips screen in `InGameSinglePlayerSetup.Process` (state 1, waiting for `CharacterManager.HasCurrent`).

### Correction to Part 5
The assumption "Unity no longer drives the runner" is outdated (h78–h82): `CharacterBuilder.Process` runs until all child coroutines complete, reaches the block after the loop (`0x1803125cc`: Create vcall `[r14+0x18]+0x178` → r15, setups from `[r14+0x20]`, then `0x1800b8470(ecx=2,..,r8=Loading,r9=r15)`). The `CharacterBuilder.Loading` future (`Loading<Character>`, flags `+0x18` Canceled, `+0x19` IsCompleted, `+0x1a` IsSucceeded, `+0x20` Error, `+0x28` Value) is **never completed** (all 0). On the last runner call, onLeave is missing → likely an exception in the AFTERLOOP (Create vcall or a setup), unconfirmed. The callback from `CreateHumanUnit` (`Loading<T>.AddCallback` `0x181818e90`) therefore never fires, `CreateUnit` is never reached.

### Hypothesis (specified by user)
The root cause is most likely in **missing/incorrect API data** (mock), not in the game routine. Check mock data first, then continue debugging.

### Mock Verification
- Weapon: without `userWeapon`, `GetWeaponModel`/`CreateForHuman` uses `Database.GetDefaultWeapon(MountType→WeaponType)` or `CharacterModel.Weapon` (`defaultWeaponId`). Mock has weapon 1 (`weaponType=1`=Sword, MountType Strike→Sword). Probably fine.
- Mount: `UserPartyUnit.UserMountMonster` empty → `Database.GetDefaultMountMonster` (mock: `isDefault=True`).
- `data/load` types 1, 3, 9, 19, 20, 22, 23, 24 are all requested, no errors in `mock_requests.log`.
- **Newly set in mock (untested effectiveness):** `Monster.modelId=1026002` (manifest: `monster/model/m_1026002`), `Character.motionListAssetName='h_025001_uniq_m'` (guessed; manifest has `character/human/uniquemotionlist/h_0xxxxx_uniq_m`).
- **Still 0/empty, next candidates:** `PlayableCharacter.extremeSkillId`/`hateId`, `Character.sequenceId` (manifest: `character/player/sequence/pm_00_000000_seq_list`, `pm_01_000001..pm_04_000004`, `pm_00_900000`) and `characterProfileId`, `PlayerSkill` details (`ids`, `statuses`), `UserCharacter` values (hp/sp/attack None), weapon `attack`/`elementalPoint` None, `UserWeapon`/`UserMountMonster` in `registered-info`.
- Usable models: `skel.default('<Model>')` in `test\skel.py` provides default dicts; stubs in `files\diff\DiffableCs\...`.

### Latest Test
`test_run2.ps1 -wait 60` after mock change: requests OK, game still on tips screen; screenshot was obscured by an unrelated Qwen window (result not confidently assessable, probably unchanged). Close unrelated windows before the next test.

### Next Steps
1. Extend mock: `Character.sequenceId` (e.g. 0/1 matching `pm_00_000000`), `PlayableCharacter.extremeSkillId/hateId` with matching data sets (possibly Extreme Skill/Hate data types via `data/load`), `userWeapons`, values != None.
2. Test; on failure, set targeted function-entry hooks (HumanCreate `0x1806adf80`, setups, `WeaponData ctor` `0x1804e3960`, `CharacterParameter ctor` `0x1806bb340`) to find the throwing location.
3. Then check `InGameSinglePlayerSetup`, `PostProcess`, `CompileShaders`, `Teardown`, HUD/Home.

### Frida/Test Rules
- Test flow: fresh mock (`restart_mock.ps1`), 10 s, game, 5 s, screenshot; no long sleeps, no clicks. End game afterwards (`Stop-Process -Id`).
- Never use Stalker, mid-function hooks (`0x180312605` etc.), hooks on `0x1800b8110` or `0x1802954D0`; `0x180295490` is very noisy. First `start_frida_session` after process kill fails silently → restart.
- Helper scripts in `...\session-state\f9a4d511-...\files\`: `q.py`, `disasm.py`, `xr.py`, `sm2.pkl`, hooks `h70`–`h82.js` (h81 d30 calls, h82 Loading future).
- Known VAs: `CharacterManager` Update `0x1806b8fc0`, HasCurrent `0x1806b73b0`, CreateHumanUnit `0x1806b69c0`, CreateUnit `0x1806b6c50`; `PlayerParameter.CreateForHuman` `0x18075f880`; `Build_1` `0x1806aefa0`; `CharacterBuilder.Process` MoveNext `0x180312370`; `InGameSinglePlayerSetup.Process` `0x180326010`.

### Part 6b (05.11.2026)
- Mock extended: `PlayableCharacter.extremeSkillId=1, hateId=1, defaultPlayerSkillLevel=1`; `boot/top` now additionally serves data types 21 (CharacterProfile), 26 (PassiveSkill, empty), 28 (Hate), 29 (Bullet, empty); `data/load` serves them (see `mock_server.py`). Game requests them (log), behavior unchanged: still hangs on tips screen.
- Hook `h83.js` (Entry/Leave): `CreateForHuman`, `CharacterParameter.ctor`, `GetDefaultMountMonster`, `get_UserWeapon` (null → default weapon), `CharacterModel.get_Weapon`, `WeaponData.CreateDefault`, `get_ExtremeSkill`, `GetWeaponModel`, `GetDefaultWeapon`, `HumanCreate`, `Build_1` all return **non-null** and return normally. The data accessors of the build preparation are therefore **not** the cause; `get_Hate`/`get_PlayerSkill`/`get_RarityDependence` are not called up to that point.
- Conclusion: the error occurs later (d30 coroutine/AFTERLOOP: Create vcall `[r14+0x18]+0x178`, setups from `[r14+0x20]`) or in asset/prefab-dependent setups (HumanPrefab `h_000015`, weapon prefab `wep_0220002`, `pm_00_000000_seq_list`, motion list). Next step: entry hooks on the individual setup classes (ParameterSetup, WeaponSetup, SpringBoneSetup, BattleStateSetup, HumanRendererSetup, PlayerModuleSetup, TownHumanPlayerControllerSetup; VAs via `q.py <Name>`) and on `HumanCreate` prefab loading, to find the last reached setup; check character/sequence asset names against the manifest (Sequence ID, MotionListAssetName).

### Part 7 (05.11.2026) – CharacterParameterSetup, Mock Fixes, Ghidra Project
- Hooks h84/h85: `MinimumCharacterCreate.Create` (`0x1804c1910`) runs without errors; first setup `CharacterParameterSetup.Process` (`0x1806bb190`) was entered but never exited → exception there (`PlayerParameter.CreateStatus` → `CharacterStatus.CreateFrom` `0x180923810` → `UnitStatusCalculator.Calc` `0x18094fa80` → `Calc_1` `0x18094fb50`).
- h86: `get_UserWeapon` returns non-null after mock fix; `Calc` was entered. `Calc_1` uses (when UserMountMonster is missing) `Database.GetDefaultMountMonster` + `MountMonsterStatusCalculator` + `MountMonsterModel.get_Hate` → cause: `MountMonsterModel.hateId` (and PlayerSkill1Id) was 0, Hate data set has id 1 → NRE.
- Mock fixes (`mock_server.py`): `userCharacters` with `hp/sp/attack/physicalDefense/magicalDefense/elementalPoint/playerSkillLevel`; `userPartyUnits.userWeaponId='1'` + `userWeapons` (id 1, weaponId 1); `MountMonster.hateId=1, playerSkill1Id=1, baseHp/Sp=100, baseAttack/Defense=10`; new route `/api/steam-payment/recover` (`SteamPaymentRecoverResponse` default) – without it, the dialog "Communication Error: not mocked" appears after `farm/top`.
- Result: **CharacterBuilder chain now runs through.** The game then loads HUD assets (`ef_et001_*`, `ui/atlas/commonicon`, `map/town/asset/tw101/models`, ~79 `AssetBundleLoader.Load` calls in 1 s, hooks h92/h94 on `0x180c4d250`), all names exist in the manifest. Then it stalls (tips screen remains). Without Frida, after ~40–105 s the dialog "Failed to load. Return to Title screen." appears (`client-error/register`: "Failed to read data for the AssetBundle '509720'", path `w/-4/37/509720` = name unknown in manifest → numeric hash path). Under Frida the error does not occur (timing). The source of the name is open: it does not come via `AssetBundleLoader.Load`, `StreamingAssetBundleEnvironment.CreateUrl` (`0x180a9f300`, never called), or the managed `AssetBundle.LoadFromFile*` wrappers (`0x181b220a0/f0`, path never seen). Presumption: Unity-native load path or a dependency entry in the bundles; manifest text `local_latest.manifest` is consistent (all 40915 names, all dependencies resolvable).
- Ghidra project with names: `\volzerk\ghidra-named\proj\VolzerkNamed.gpr` (GameAssembly.dll, 103,287 functions / 68,437 labels named, from `ida-proj\il2cpp.json`; generation: `gen_names.py` → `names.tsv` → `analyzeHeadless ... -process GameAssembly.dll -noanalysis -postScript ApplyNames.java names.tsv`). Custom names/comments in the `CURATED` dict of `gen_names.py`. Folded functions are named `<Name>__sharedN`.
- Frida hooks h83–h94 (`...\files\`). Note: lingering child processes `volzerk.exe` may not be terminable (access denied) – they disappeared later.

## Part 8 – Chain After CharacterBuilder Through to HomeController.Setup

- After the mock fix (MountMonster.hateId=1), CharacterBuilder, `MinCharCreate.Create`, and `InGameSetupSequence` (4 setups) complete. `InGameStateSetup.Setup` → SetupCompleted, `InGameStateStart.StateStart` (MN 0x180329f50) → state 3 = `HomeController.Setup` (MN 0x1804ac500, fields: loadRequest@0x30 ResourceRequest, loading@0x38 ResourceLoading\<BezierPath\>, param@0x40 SceneParam).
- `HomeSetup` state 3 calls `Resources.LoadAsync(path, type)` (stub 0x181271c00 → 0x18118c2e0). Hooked: first `LookAt/LookAtNearCharacterSettingData` (complete), then `Town/HomeGeneralSettingData` (request never becomes `isDone`, polling via `AsyncOperation.get_isDone` 0x181346140). Both names are in `resources.assets` (index present), so the asset itself exists.
- Hypothesis: Unity's async load queue is blocked by a hanging operation (bundle load). Without Frida, "Failed to read data for the AssetBundle '509720'" appears later (path `StreamingAssets/1/w/-4/37/509720`; path scheme hash[0:2]/hash[2:4]/hash with hash="−437509720" – not a hex hash, not in manifest). `StreamingAssetBundleEnvironment.CreateUrl` (0x180a9f300) is NOT called in this context → the path is generated elsewhere (open).
- Additional log entry: "The referenced script (Unknown) on this Behaviour is missing! ('wall_col')" → a loaded map prefab has missing scripts.
- New mock route `/api/steam-payment/recover` (SteamPaymentRecoverResponse default).
- Open: origin of the numeric bundle hash −437509720 (presumably a value from an API response interpreted as a hash string, e.g. map/farm ID); hook scripts h112/h113 in session files.

## Part 9 – Bundle Error 509720: Previous Tests and Correction

- `ResourceManager.GetHashedPath` builds paths directly from a hash string: `hash[0:2]/hash[2:4]/hash[4:]`. The error path `w/-4/37/509720` therefore maps unambiguously to the hash **`-437509720`** (not a 32-hex-digit manifest hash).
- A brief reproduction test placed `w/-4/37/509720` as a copy of `map/town/asset/tw101/models` (`36ea9bff8d935c7cd4346b01dcb3`). The copy was subsequently removed. Result:
  - `The AssetBundle '36ea9bff8d935c7cd4346b01dcb3' can't be loaded because another AssetBundle with the same files is already loaded.`
- This result does not prove that the game logic deliberately loads the same bundle twice: it only shows that Unity recognized the copied bundle file as already-loaded content. The cause of the incorrect name/hash remains open.
- An experimental value `assetBundleLatestHash='local_latest_custom_manifest'` was reverted in `mock_server.py` to the previous test value (`'0'*32`). The request header remained `AssetBundle-Manifest: local_latest` throughout, so the attempt was not a valid fix.
- There is still no evidence of a bug in the game code or of a missing API endpoint. However, `farm/top` in the mock only provides a largely empty skeleton besides `map.mapId`/`map.type`; `MapGenerateInfoModel` and `HomeDataSetModel` contain additional fields that may be relevant for the home start. The API responses must therefore be completed and checked against the expected data flow before assuming a game code error.

Next sensible step:
- Without modifying `GameAssembly.dll`/`global-metadata.dat`, capture the values from `/api/farm/top` that feed into `HomeController`/`ResourceManager`, and trace the origin of `-437509720` back to a specific API property or asset path resolution.

## Part 10 – Hash Reverse-Calculation and Town Scene ID

- The ISIL disassembly of `System.String.GetHashCode` confirms the IL2CPP hash algorithm: two accumulators initialized with `0x1505` process alternating UTF-16 characters with `hash = hash * 33 XOR char`; the result is `h2 * 0x5D588B65 + h1` as a signed 32-bit value.
- `DefaultManifest.GetAssetBundleVersion` uses `GetHashCode()` of the bundle name as a decimal string when the manifest hash is missing/null. This explains why the path `w/-4/37/509720` contains a short negative value instead of a 32-digit Hash128.
- Reverse lookup for the specific town scene name `map/town/scene/{ID:D11}`:
  - The mock at the time had `MapGenerateInfo.SceneId=0`; the resulting name would be `map/town/scene/00000000000` with hash `-831303549`, not `-437509720`. For the home branch, however, `mapGenerateInfo.map.mapId` is what matters, not `SceneId` (see Part 11).
  - `mapId=10010100102` exists as `map/town/scene/10010100102` in the `local_latest` manifest requested by the game. Its string hash is `1362693933`, also not `-437509720`.
  - Inverting the 32-bit hash under exactly this name scheme yields several possible 11-digit numbers (hash collisions); none of them appear among the 14 town scene entries in the local manifest. Therefore, no valid `SceneId` can be derived from the error hash.
- The manifest hash for `map/town/scene/10010100102` is `eeb3af711ebf786936804b0a68887e47`; the corresponding local bundle file `w/ee/b3/af711ebf786936804b0a68887e47` exists (158,397 bytes).
- A search across all 40,915 `Name` entries in the local `local_latest.manifest` found no bundle name with string hash `-437509720`. This means the error hash is not an entry in this local manifest; it does not prove which runtime-generated bundle name is behind it.
- **Correction:** `10010100102` was an existing value for `mapId`, not for `SceneId`. The bundle is a field scene and not suitable evidence for a home map; see Part 11. The hash inversion does not prove a specific requested bundle name due to possible collisions.

Next step:
- Statically trace the bundle name from the home/map load data flow through to `AssetBundleLoaderImpl.GetAssetBundleVersion`. Only if the existing disassemblies do not yield the string unambiguously, use a narrowly scoped passive runtime hook on exactly this function parameter.

## Part 11 – Home Map and Character Image (15.11.2026)

- `MapManager.Initialize` reads `MapManager.MapId` from `mapGenerateInfo.map.mapId` in the home branch and calls `LoadMapScene` with it. The old mock `mapId=10010100102` points to a locally present bundle with field objects (`fi101`), while `10100101101` is a local scene with home/farm/quest objects. The mock was changed to `mapId=10100101101`, `type=1`. The bundle `w/c4/c5/2a615c4916a62adad2b08e709039` is locally present. A test with this map correction and still `characterId=15` still reported `509720`; the map correction alone is not a fix.
- The bundle format string for `AssetPath.CharacterImage` is `ui/character/image/characterimg_{0:D8}`. For `15`, this yields `ui/character/image/characterimg_00000015`, which per the algorithm described in Part 10 hashes to exactly `-437509720`. This name is missing from the local manifest. The hash match is strong evidence, but due to possible collisions it is not a direct runtime proof of the failed request.
- The ISIL of `UIExSkillCutIn.CheckRequireResource` shows `UserCharacterModel.PlayableCharacter → PlayableCharacterModel.Character → CharacterModel.CharacterId` (offset `0x28`) as input to `CharacterImage.NameData`. The same data source is visible in `SetUpCutinImage`. Whether one of these specific calls produced the failed home request was not confirmed at runtime.
- The mock now uses `MOCK_CHARACTER_ID=1001` in `CharacterModel` and `PlayableCharacterModel`, also for the character models delivered via `farm/top`. Profile ID, model ID, and motion list remain unchanged; their semantic alignment with image ID 1001 is unproven. The name `ui/character/image/characterimg_00001001` is in the binary manifest; its hash is `51a6093148c7625bcbe4ac4b58f89d61`, and the file `w/51/a6/093148c7625bcbe4ac4b58f89d61` exists.
- Mock syntax check successful. Uninstrumented test with `characterId=1001`: after 70 seconds the game process was still active; `/api/farm/top` and `/api/steam-payment/recover` were reached; neither `509720` nor any other exception appeared in Player.log or as a client-error request. A further uninstrumented test showed the loading tips screen after 60 seconds with no relevant Player.log error. This neither confirms a full home start nor definitively that the bundle error is permanently resolved: it was previously observed after roughly 40 to 105 seconds.
- A third uninstrumented test over 130 seconds exceeded this previously observed error window: no `509720`, no client-error request, and no relevant Player.log exception; the game still showed the loading tips screen. This supports the image ID hypothesis but proves neither the actual origin of the old request nor a complete start.
- An earlier Frida observation of 48 seconds on the test copy saw 203 version queries but not `-437509720`; the error did not occur during this observation window under instrumentation (REA evidence `ev_4b456b8c010dc0b80414730306e8f50bcc4b8d5fd590b66256ea44096be55d64`). Timing and coverage limit the conclusion.
- The tests only started and terminated their own game and mock PIDs; no mouse clicks. The test copy's DLL was unchanged before and after the first test. Note: this copy already contains older modifications for auth ticket waiting, SSL validation, and consent, as well as patched metadata for server redirection. A start with unmodified original files has therefore not been demonstrated.
- Two subsequent Frida attempts produced no usable new setup state: during spawn, no API calls were observed (REA evidence `ev_86d7975b55384309e47dd2e1ed73c7a32c1941ff74c01f63afbed3d09d203fc6`); during attach, the target process detached before the expected result message (REA evidence `ev_221c0633f1164559448327626c0c4aaa9f6915d4f7148e366493ed4f69ad83ef`). These failures do not support any conclusion about whether HomeSetup is reached.
- A further attach test reached `/api/farm/top`; in two later observation windows, no calls to `HomeSetup` or `Seq`, `Parallel`, `AllDone`, `StateSetup`, and `StateStart` were seen (REA evidences `ev_c2a564f749922b4b55df73314f59c3b01086147eacbeec6c0de92411d05ff7e7` and `ev_74620d952ad58f3343557ac064cd77276d2b6e37b64926b473391786a7b9c1e2`). The attach occurred after game start: a call before the observation window or another waiting coroutine/native object remains possible. The current wait point cannot be determined from this.

Next step: Identify the current wait state early from process start based on the existing setup/async load chain and statically verify the associated mock data. For the image finding, specifically confirm the bundle name at runtime; the 130-second test alone is not direct proof.

## Part 12 – Farm Data, Gold, Prologue, and Visible Home Start

- The following tests used the already patched test copy and a local MessagePack mock. No additional DLL or metadata patches were made during this investigation. The observations with `home_probe.py` are local Frida observations and not REA evidence records.
- `HomeController.Initialize` adopts `Database.FarmDataSet` from `bootMasterDataSet.farmDataSet` in the `boot/registered-info` response. Before the fix, this pointer was null; `HomeController.<Setup>d__60` did not reach `MountMonsterExpUpdater.SetInterval` after `SetEnableFarmMonsterVoice`. The mock now provides a `FarmDataSetModel` with `updateIntervalSeconds=60`. After that, the pointer and interval as well as the return of `SetInterval` were observed, and HomeSetup reached state 4. 60 is a mock placeholder, not a reconstructed original value.
- Subsequently, the home UI transition stalled in `UIOutGameHeaderController.UpdateHeader`. `UIOutGameHeaderViewModel.UpdateFromUser` reads `MyUser.CurrentGold`; the getter looks for a `CurrentGoldModel` entry with a matching `userId`. Before the fix, the getter returned null for the mock user and the header call did not observably return. The mock now sets `userGeneralItemDataSet.currentGold` with `userId='1'` and gold value 0 in both `boot/registered-info` and `farm/top`. After that, the getter returned a non-null pointer, the header returned, `home_ui_complete` was called, and HomeSetup completed. The null reference is based on static analysis and runtime observation; the exact exception type was not captured.
- A subsequent uninstrumented 65-second test showed a black screen with a loading indicator. The start chain was waiting in `InGameStateStart.<StateStart>d__2` on `<RunGameStart>d__5`, which called `PrologueController.<OnInGameStateStart>d__14`. The latter method was entered and did not return in the observation. This alone proves neither a native deadlock nor the exact exception type.
- `GameManager.SetPrologueSetting` activates the prologue when `UserFlagType.ClearPrologue` (type 7) is absent or false. The mock had already provided a home/farm for an existing profile but no prologue flags. It now reports consistently `{userId: '1', userFlagId: '1', type: 7, value: true}` in `userDataSet.userFlags` and `farm/top.userFlags`. This deliberately simulates a user with a completed prologue; it does not prove that the prologue works with a new account. Afterwards, `RunGameStartTown`, `RunGameStart`, and `StateStart` were observed through to normal coroutine completion; the prologue call did not occur in this test.
- Verification without Frida: after 65 seconds, the test copy showed the home game world with the player figure and the hint `[Esc] Open Menu`; the process remained active until it was terminated. Screenshot: `\.copilot\session-state\f9a4d511-[...]\files\home_plain_result.png`. No matching exception or `509720` was found in Player.log; FMOD reported a missing audio device and emulated audio output. The test confirms the visible world, not the functionality of movement, menus, quests, or saving. The start processes were terminated by their own PIDs.
- The mock still contains synthetic data and does not implement all API functions. An unmodified original client was not tested; the test copy still requires the previously documented patches. A real new account with prologue as well as the completeness and playability of home features remain open.

## Part 13 – Prologue Path (17.11.2026)

- Observation (Frida, instruction hooks): with `MOCK_SKIP_PROLOGUE=0`, `PrologueController.<OnInGameStateStart>d__14` reaches state 0 and finds `QuestManager.I.QuestStage == null`; the state fails there with a null reference, `IsExistFile` is never reached. `set_QuestStage` is practically only called after a quest-enter response.
- Observation: `StartupScene.NextSceneRoutine` (`0x18045fc50`) branches on `MyUser.CurrentQuest.QuestId` (offset `0x40`): `0` leads to home, otherwise to `QuestManager.ContinueQuest(questId, onComplete)`. This is the presumed path of the original for new players (server delivers an ongoing prologue quest).
- Mock: `MOCK_CUR_QUEST=<id>` sets `userCurrentQuest.questId`; new handler `quest_enter` for `/api/quest/enter` and `/api/tutorial/quest-enter` (stage with `enteringMap.mapSceneId` from `MOCK_QUEST_MAP`, `questCurrentFloor.sceneId/mapId`). A field `isQuestEnter` in `questProgress` leads to "One of the identified items was in an invalid format" (not a serialization field).
- Observation: `ContinueQuest.<>d__141.MoveNext` (`0x1805bbbd0`) is entered in state 0, creates `QuestEnterApi`, sends `POST /api/quest/enter {"questId":1}`, and waits via `WaitForCompletion`; state 1 is never reached (loading indicator bottom right, otherwise black screen). The mock responds correctly to the request (verified directly via Python, 5013 bytes). Neither a response header `AssetBundle-Manifest` nor other map IDs (`10010100102`, `29999999999`) change this. During boot, only one NRE thrower call was observed (2.3 s, before the request).
- Locally present: all 41,548 bundles from `local_latest.manifest` (including `system/predownload/tutorial/prologue|episode_0`, field scenes `map/field/scene/29999999998|9`).
- Open: why the `QuestEnterApi` future is not completed (response processing after parsing), which prologue quest ID and map the original used.

## Part 14 – Prologue Parameters from Local Predownload Lists

Source: `PreDownloadList` MonoBehaviours in `system/predownload/tutorial/*` (path via `StreamingAssets\1\w` and Hash128 from `local_latest`, script `bm.py`).

- `tutorial/prologue`: field scene `map/field/scene/20010130101` (prologue gameplay: movement, minimap, combat effects, tips `move`).
- `tutorial/episode_0`: episode scenes `episode/scene/90010001101_ep_001`, `90010002101_ep_001`, `90010003101_ep_001`, `10100101101_ep_002`; scenarios `episode/scenario/1_000_001_001..004`; dungeon `map/dungeon/scene/3001019210001` (preset `dungeonvisualpreset_1`, asset `dg1012`), enemy `en_200200110`.
- `tutorial/startup_predownload_list`: quests `system/predownload/quest/900001101` and `900001102` with dungeons `3001011410003` and `3001011910001`; town `map/town/scene/10100101101`.
- Conclusion (inference): prologue quest IDs are in the range `9000011xx` (900001101, 900001102, ...), not `1`. Scene IDs follow the scheme Type/Area/Number. The server delivers the quest via `userCurrentQuest.questId` and `quest/enter`; `PrologueController.ExecuteQuestClear` reads the follow-up quest from `MyUser.CurrentQuest.QuestId`.
- Unresolved: mapping quest ID → map ID/episodes (comes from master/server data) and which ID actually starts the prologue.

## Part 15 – Test with Quest 900001101 / Scene 20010130101 (Mock: MOCK_CUR_QUEST, MOCK_QUEST_MAP)

Observed (runtime, Frida/screenshots):
- With `questId=1`, `ContinueQuest` hung; with `900001101`, the `QuestEnterApi` future completes. After that, three errors appear in sequence, each revealing a mock response property:
  1. "One of the identified items was in an invalid format" = `FormatException` in `JsonConverter.AppendStream → FormatReader.ReadExtType`. The path `MessagePackFormatter.Deserialize → JsonConverter.Encode` passes the ext format (0xD6) instead of the type byte; every MessagePack ext type (timestamp) in the response throws. Solution: timestamps in `quest/enter` as ISO string (`no_ext` in mock). Other responses (e.g. account) do not use this path.
  2. "Vector3Handler: Undefined Format 0xC0": Vector3 is an array of 3 floats and must not be nil. Solution: `skel.default` returns `[0,0,0]` for Vector3 (Vector2/Quaternion/Vector4 analogously, unverified).
  3. With `stageType=0`, `InGameStateInitialize` stalled (no scene loaded). With `stageType=1`, `questType=1`, the game loads character, weapon, effects, sounds, and `map/field/scene/20010130101`.
- Current status: after that, dialog "Failed to load. Return to Title screen."; the game sends `POST /api/client-error/register` with `{"message":"Failed to read data for the AssetBundle '358079'."}`. The requested file `StreamingAssets\1\w\13\51\358079` does not exist (name without manifest entry, `String.GetHashCode` path, hash `1351358079`). The associated bundle name is still unknown; it does not come from the `PreDownloadList`s of prologue/episode_0/startup (hash comparison with no match).
- Without a `SetupPrologue` call: `episodes` is empty, so the prologue controller (timing/asset name) is not set.

## Part 16 – Bundle 358079 Resolved, Next Hang

- `358079` = `character/player/sequence/pm_01_000000_seq_list` (via Frida hook on `String.GetHashCode`). In the manifest, only `pm_00_000000`, `pm_01_000001` ... `pm_04_000004` exist (pattern `pm_<mountType>_<sequenceId>`).
- Origin: `CharacterBuilder.Player` → `PlayerBuildParam.SequenceId` = `MountMonster.Monster.SequenceId`; this comes from `MountMonsterModel.SequenceId` (offset 0x54, `MountMonsterBuildParam(MountMonsterModel)`), not from `MonsterModel`. Mock: `mountMonsters[0].sequenceId=1` (mountType=1) → `pm_01_000001_seq_list`. No more client errors.
- NRE in `CharacterManager.LoadOptionMonster` → `OptionMonsterParameter.CreateFrom`: `UserPartyUnitModel.HasLeftOptionMonster` is `LeftUserOptionMonsterId != ""`, a `nil` counts as present. Mock now sends `leftUserOptionMonsterId/rightUserOptionMonsterId/userAccessory1Id/userAccessory2Id = ""`.
- Status: all bundles including `map/field/scene/20010130101` load, no error dialog, but the loading screen remains indefinitely (>90 s), no further requests. Remaining NRE at ~4.0 s: `PlayerSkillSequenceAsset.Execute` (0x180761370, object allocation at 0x18076171f returns null) inside `CharacterBuilder.Process`. Cause open; next step: check skill sequence data (`PlayerSkillModel`, sequence assets).
