# custom sha256 hash function

import hashlib


def hash_message(message):
    """
    hash a message
    :param message: message to hash
    :return: sha256 hash of message
    """
    return hashlib.sha256(message.encode()).hexdigest()


print(hash_message("Hello World"))


def hmac_message(key, message):
    """
    hash a message with a key
    :param key: key to hash with
    :param message: message to hash
    :return: sha256 hash of message
    """
    return hashlib.sha256(key.encode() + message.encode()).hexdigest()


print(hmac_message("key", "Hello World"))


def hmac_verify(key, message, hmac) -> bool:
    """
    verify a hmac hash
    :param key: key to hash with
    :param message: message to hash
    :param hmac: hmac hash to verify
    :return: True if hmac is valid, False otherwise
    """
    return hmac_message(key, message) == hmac


print(hmac_verify("key", "Hello World", hmac_message("key", "Hello World")))


def custom_sha256(message):
    chars = "0123456789abcdef"
    hash = hash_message(message)
    result = ""
    for i in range(0, len(hash), 2):
        result += chars[int(hash[i:i + 2], 16) % 16]
    return result


print(custom_sha256("Hello World"))


def decipher_custom_sha256(message):
    chars = "0123456789abcdef"
    result = ""
    for i in range(0, len(message), 2):
        result += chars[int(message[i:i + 2], 16) % 16]
    return result


print(decipher_custom_sha256(custom_sha256("Hello World")))