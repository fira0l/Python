import sys
import os

MOO_ENCRYPTION_KEY = 0xFF
MOO_PADDER = 0x04


def boo_decrypt(data: bytes) -> bytes:
    """Decrypt data that was encrypted by moo."""
    decrypted = bytearray()
    for b in data:
        original = ((b ^ MOO_ENCRYPTION_KEY) - MOO_PADDER) & 0xFF
        decrypted.append(original)
    return bytes(decrypted)


def boo_file(input_path: str, output_path: str = None):
    """Decrypt a file encrypted by moo and write output."""
    if not os.path.exists(input_path):
        print(f"Error: file '{input_path}' not found.")
        return False

    with open(input_path, "rb") as f:
        encrypted_data = f.read()

    decrypted_data = boo_decrypt(encrypted_data)

    if output_path is None:
        # by default save as <filename>.boo.dec
        output_path = input_path + ".boo.dec"

    with open(output_path, "wb") as f:
        f.write(decrypted_data)

    print(f"Decryption complete. Saved to: {output_path}")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python boo.py <encrypted_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    success = boo_file(input_file, output_file)
    sys.exit(0 if success else 1)

