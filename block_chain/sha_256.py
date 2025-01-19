import hashlib
from typing import Optional

def hash_message(message: str) -> str:
    """
    Generate a SHA-256 hash for a given message.

    Args:
        message (str): The message to hash.

    Returns:
        str: The SHA-256 hash of the message.
    """
    return hashlib.sha256(message.encode()).hexdigest()


def hmac_message(key: str, message: str) -> str:
    """
    Generate a keyed SHA-256 hash (HMAC) for a given message and key.

    Args:
        key (str): The key to hash with.
        message (str): The message to hash.

    Returns:
        str: The HMAC of the message.
    """
    return hashlib.sha256(key.encode() + message.encode()).hexdigest()


def hmac_verify(key: str, message: str, hmac: str) -> bool:
    """
    Verify an HMAC against a given key and message.

    Args:
        key (str): The key to hash with.
        message (str): The message to hash.
        hmac (str): The HMAC to verify.

    Returns:
        bool: True if the HMAC is valid, False otherwise.
    """
    return hmac_message(key, message) == hmac


def custom_sha256(message: str) -> str:
    """
    Generate a custom SHA-256 hash modification.

    Args:
        message (str): The message to hash.

    Returns:
        str: The custom SHA-256 hash of the message.
    """
    chars = "0123456789abcdef"
    hash = hash_message(message)
    result = ""
    for i in range(0, len(hash), 2):
        result += chars[int(hash[i:i + 2], 16) % 16]
    return result


def decipher_custom_sha256(message: str) -> str:
    """
    Decipher a custom SHA-256 hash modification.

    Args:
        message (str): The custom SHA-256 hash to decipher.

    Returns:
        str: The deciphered hash.
    """
    chars = "0123456789abcdef"
    result = ""
    for i in range(0, len(message), 2):
        result += chars[int(message[i:i + 2], 16) % 16]
    return result


if __name__ == "__main__":
    print(hash_message("Hello World"))
    print(hmac_message("key", "Hello World"))
    print(hmac_verify("key", "Hello World", hmac_message("key", "Hello World")))
    print(custom_sha256("Hello World"))
    print(decipher_custom_sha256(custom_sha256("Hello World")))
