# Volzerk-Patches

These scripts make the necessary changes to the game files.
You need to have Python 3.9 or newer with no additional packages installed and the following file
`patch_common.py` in the same folder as the sub-scripts.

Before applying patches close the game fully.

**NOTE: Only apply the patches to a copy of the game, the scripts will reject the original Steam folder. The changes to the files are permanent and can only be reverted by re-downloading the game files.**



| Script | Change |
|---|---|
| `patch_steam_ticket.py` | Skips waiting for the Steam ticket callback. |
| `patch_ssl.py` | Forces `SslVerifyer.IsValid` to return `true`. |
| `patch_consent.py` | Automatically accepts/skips the Consent-Form |
| `patch_server_hosts.py` | Redirects all network calls to `127.0.0.1:8092`. |
| `patch_api_url.py` | Removes the `api.` prefix of some requests. |
| `patch_http_literal.py` | Changes the `https`-literal to `http`. In some instances the game still forces HTTPS/TLS, therefore also running `patch_ssl.py` is recommended |

## Execution

Open PowerShell and check the patch without applying any changes:

```powershell
python ".\patch_ssl.py" --game-dir "<GameDir>"
```

To apply patches execute with `--apply`:

```powershell
python ".\patch_ssl.py" --game-dir "<GameDir>" --apply
```

Repeat the process for each wanted patch individually.
Patches can be applied in no specific order and will only run once - duplicate executions are detected and skipped.

Pre-Patch verification works by creating a SHA256-Hash of each known patch region and compares them to the scripts values.
If the hash differs the patch will not resume execution and abort.
