# author: Yiwei Zhang
# date: 2024-01-16
from passwordler._internals import original, getKeyMap
import pytest
import random

# import decrypt_password as below after merged
# from src.passwordler.decrypt_password import decrypt_password

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
