# author: Yiwei Zhang, Michelle Hunn
# date: 2024-01-16
from passwordler.encrypt_password import encrypt_password, decrypt_password
from passwordler._internals import original, getKeyMap
import pytest
import random

# import decrypt_password as below after merged
# from src.passwordler.decrypt_password import decrypt_password


def test_encrypt_normal():
    """
    Test that a standard message is correctly encrypted.
    The encrypted message should be different from the original message.
    """
    message = "testmessage"
    encrypted = encrypt_password(message, 123)
    assert encrypted != message
    assert isinstance(encrypted, str)


def test_encrypt_empty_string():
    """
    Test that an empty string remains unchanged when encrypted.
    """
    message = ""
    encrypted = encrypt_password(message, 123)
    assert encrypted == ""


def test_encrypt_non_standard_characters():
    """
    Test that non-standard characters (not in the original character set) 
    are unchanged in the encrypted message.
    """
    message = "test~`**^"
    encrypted = encrypt_password(message, 123)
    print(encrypted)

    assert all(char in encrypted for char in "~`**^")

# Test cases for decrypt_password


def test_decrypt_normal():
    """
    Test that an encrypted message is correctly decrypted back to the original message.
    """
    message = "testmessage"
    encrypted = encrypt_password(message, 123)
    decrypted = decrypt_password(encrypted, 123)
    assert decrypted == message


def test_decrypt_empty_string():
    """
    Test that an empty string remains unchanged when decrypted.
    """
    encrypted = ""
    decrypted = decrypt_password(encrypted, 123)
    assert decrypted == ""


def test_decrypt_non_standard_characters():
    """
    Test that non-standard characters (not in the original character set) 
    are unchanged in the decrypted message.
    """
    message = "test~`**^"
    encrypted = encrypt_password(message, 123)
    decrypted = decrypt_password(encrypted, 123)
    assert all(char in decrypted for char in message)
