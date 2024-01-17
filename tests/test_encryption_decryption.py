# author: Yiwei Zhang, Michelle Hunn
# date: 2024-01-16
from passwordler.encrypt_password import encrypt_password, decrypt_password, original, getKeyMap
import pytest
import random

# import sys
# import os
# # Import the count_classes function from the src folder
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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

# Test cases for getKeyMap


def test_get_key_map_for_encryption():
    """
    Test that getKeyMap generates a correct mapping for encryption.
    Each character in the original list should map to a different character in the shuffled list.
    """
    shuffled = original.copy()
    random.shuffle(shuffled)
    key_map = getKeyMap(shuffled, isDecryption=False)
    assert len(key_map) == len(original)
    assert all(key_map[orig] != orig for orig in original)


def test_get_key_map_for_decryption():
    """
    Test that getKeyMap generates a correct mapping for decryption.
    Each character in the shuffled list should map to a character in the original list.
    """
    shuffled = original.copy()
    random.shuffle(shuffled)
    key_map = getKeyMap(shuffled, isDecryption=True)
    assert len(key_map) == len(original)
    assert all(key_map[shuff] in original for shuff in shuffled)


def test_get_key_map_length():
    """
    Test that the key map generated has the same length as the original character list.
    """
    shuffled = original.copy()
    random.shuffle(shuffled)
    key_map = getKeyMap(shuffled)
    assert len(key_map) == len(original)
