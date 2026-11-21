import argparse
import hashlib
import os
from pathlib import Path
import shutil
import tempfile


DLL = Path("GameAssembly.dll")
METADATA = Path("volzerk_Data") / "il2cpp_data" / "Metadata" / "global-metadata.dat"
ORIGINAL_GAME = Path(r"D:\_Dev\_Reversal\volzerk\Orig\volzerk")

# Offsets and hashes apply only to the investigated Volzerk 1.3.1 files.
PATCHES = {
    "steam_ticket": (
        DLL,
        [(0x46911D, "75", "eb")],
    ),
    "ssl": (
        DLL,
        [(0x505E50, "488bc4", "b001c3")],
    ),
    "consent": (
        DLL,
        [(
            0x5096EA,
            "e8618717004885c0742e488b1585ff00024533c94c8bc7488bc8e8d741dd00",
            "4889f1ba010000004533c0e886aaf5ff909090909090909090909090909090",
        )],
    ),
    "server_hosts": (
        METADATA,
        [
            (0x1B4F0, "1d", "0e"),
            (0x1BBF8, "13", "0e"),
            (0xB88D6, "616d6d6f2e636f6c6f706c2e6a70", "3132372e302e302e313a38303932"),
            (0xC3033, "7374617469632e616d6d6f2e636f", "3132372e302e302e313a38303932"),
            (0xC41CD, "746f6f6c2e616d6d6f2e636f6c6f", "3132372e302e302e313a38303932"),
            (0x724136, "6c6f63616c686f7374", "3132372e302e302e31"),
            (0x724148, "6c6f63616c686f7374", "3132372e302e302e31"),
            (0x72415A, "6c6f63616c686f7374", "3132372e302e302e31"),
        ],
    ),
    "api_url": (
        METADATA,
        [(0x1D0B8, "0d", "09"), (0x1D0BC, "39", "46")],
    ),
    "http_literal": (
        METADATA,
        [(0x183B0, "05", "04")],
    ),
}

ORIGINAL_HASHES = {
    DLL: "e637e3d7f6045d522394cf342acb6bd149a0e6b0d4f93059a452c98beae7dd9a",
    METADATA: "245162faee7b17f879acfc23a97ed4b1b04177462f99fc92e2be3cfb41e9d255",
}


def validated_states(data, relative_path):
    normalized = bytearray(data)
    states = {}
    for name, (path, changes) in PATCHES.items():
        if path != relative_path:
            continue
        matches_original = False
        matches_patched = False
        for offset, old_hex, new_hex in changes:
            old, new = bytes.fromhex(old_hex), bytes.fromhex(new_hex)
            if len(old) != len(new):
                raise ValueError(f"Invalid patch definition: {name}")
            actual = data[offset:offset + len(old)]
            matches_original = actual == old
            matches_patched = actual == new
            normalized[offset:offset + len(old)] = old
        if not matches_original and not matches_patched:
            raise ValueError(f"Unexpected or incomplete patch region: {name}")
        states[name] = "original" if matches_original else "patched"
    digest = hashlib.sha256(normalized).hexdigest()
    if digest != ORIGINAL_HASHES[relative_path]:
        raise ValueError(
            "File does not match the supported original version "
            "or contains additional changes."
        )
    return states


def main(name, description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--game-dir", type=Path, required=True,
                        help="Path to a game copy")
    parser.add_argument("--apply", action="store_true",
                        help="Apply patch; without this option only check the file")
    args = parser.parse_args()
    relative_path, changes = PATCHES[name]
    try:
        game_dir = args.game_dir.resolve(strict=True)
        if not game_dir.is_dir():
            raise ValueError("--game-dir must be a game directory")
        if game_dir == ORIGINAL_GAME.resolve():
            raise ValueError("The known original folder must not be patched")
        target = (game_dir / relative_path).resolve(strict=True)
        if not target.is_relative_to(game_dir):
            raise ValueError("Target file is outside the specified game directory")
        data = target.read_bytes()
        states = validated_states(data, relative_path)
        print(f"File: {target}")
        print(f"Status {name}: {states[name]}")
        if states[name] == "patched":
            print("No changes required.")
            return
        if not args.apply:
            print("Check only; use --apply to execute.")
            return
        patched = bytearray(data)
        for offset, old_hex, new_hex in changes:
            old, new = bytes.fromhex(old_hex), bytes.fromhex(new_hex)
            patched[offset:offset + len(old)] = new
        validated_states(patched, relative_path)
        tmp = None
        try:
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=target.name + ".",
                                             suffix=".tmp", delete=False) as stream:
                tmp = Path(stream.name)
                stream.write(patched)
                stream.flush()
                os.fsync(stream.fileno())
            shutil.copymode(target, tmp)
            if target.read_bytes() != data:
                raise ValueError("File was changed in the meantime; aborting")
            os.replace(tmp, target)
            tmp = None
        finally:
            if tmp is not None:
                tmp.unlink(missing_ok=True)
        print("Patch applied successfully.")
    except (OSError, ValueError) as error:
        parser.exit(1, f"Error: {error}\n")
