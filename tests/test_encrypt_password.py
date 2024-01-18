# author: Yiwei Zhang, Michelle Hunn
# date: 2024-01-16
from passwordler.encrypt_password import encrypt_password
import pytest

def test_encrypt_password_type_error():
    """
    Test if the function returns a TypeError if the type of the input is not correct.
    """
    with pytest.raises(TypeError, match="string expected as encrypted message"):
        encrypt_password(123)

    with pytest.raises(TypeError, match="integer expected as random_seed"):
        encrypt_password("abc", random_seed="123")


def test_encrypt_password_value_error():
    """
    Test if the function returns a ValueError if the input for the encrypted_message is an emptry string.
    """
    with pytest.raises(ValueError, match="encrypted_message cannot be empty string"):
        encrypt_password('')


def test_encrypt_password_no_seed():
    """
    Test if the function returns a string as output if the seed is left as default.
    """
    result = encrypt_password('Camelot')
    assert isinstance(result, str)


def test_encrypt_normal():
    """
    Test that a standard message is correctly encrypted.
    The encrypted message should be different from the original message.
    """
    message = "testmessage"
    encrypted = encrypt_password(message, 123)
    assert encrypted != message
    assert isinstance(encrypted, str)


def test_encrypt_non_standard_characters():
    """
    Test that non-standard characters (not in the original character set) 
    are unchanged in the encrypted message.
    """
    message = "test~`**^"
    encrypted = encrypt_password(message, 123)
    print(encrypted)

    assert all(char in encrypted for char in "~`**^")
