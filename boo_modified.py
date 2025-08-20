#!/usr/bin/env python3
import sys
import os
import hashlib
import shutil


MOO_ENCRYPTION_KEY = 0xFF
MOO_PADDER = 0x04

MOO_KNOWN_HASH = "4d6bc17c127e5a5a033c25b3b841837f98938fa22318607366ffd21cfbcd4de3"


def file_hash(path: str) -> str:
    """Compute SHA256 hash of a file."""
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                h.update(chunk)
    except Exception:
        return ""
    return h.hexdigest()


def boo_decrypt(data: bytes) -> bytes:
    """Decrypt data encrypted by moo."""
    decrypted = bytearray()
    for b in data:
        original = ((b ^ MOO_ENCRYPTION_KEY) - MOO_PADDER) & 0xFF
        decrypted.append(original)
    return bytes(decrypted)


def decrypt_file(input_path: str, output_path: str = None) -> bool:
    """Decrypt a single file."""
    if not os.path.exists(input_path):
        print(f"[ERROR] File not found: {input_path}")
        return False

    with open(input_path, "rb") as f:
        encrypted = f.read()

    decrypted = boo_decrypt(encrypted)

    if output_path is None:
        output_path = input_path + ".dec"

    with open(output_path, "wb") as f:
        f.write(decrypted)

    print(f"[OK] Decrypted → {output_path}")
    return True


def scan_and_handle(path: str, quarantine_dir="quarantine") -> None:
    """Scan for moo malware by comparing hashes, then quarantine it."""
    if not os.path.exists(quarantine_dir):
        os.makedirs(quarantine_dir)

    if os.path.isfile(path):
        check_file(path, quarantine_dir)
    else:
        for root, dirs, files in os.walk(path):
            for name in files:
                fpath = os.path.join(root, name)
                check_file(fpath, quarantine_dir)


def check_file(path: str, quarantine_dir: str) -> None:
    """Check if a file matches moo hash and quarantine if needed."""
    h = file_hash(path)
    if h == MOO_KNOWN_HASH:
        print(f"[ALERT] Moo detected: {path}")
        new_path = os.path.join(quarantine_dir, os.path.basename(path))
        shutil.move(path, new_path)
        print(f"[ACTION] Quarantined to: {new_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python defender.py scan <path>")
        print("  python defender.py decrypt <file> [output]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "scan":
        target_path = sys.argv[2]
        scan_and_handle(target_path)

    elif command == "decrypt":
        input_file = sys.argv[2]
        output_file = sys.argv[3] if len(sys.argv) > 3 else None
        decrypt_file(input_file, output_file)

    else:
        print("[ERROR] Unknown command. Use 'scan' or 'decrypt'.")

