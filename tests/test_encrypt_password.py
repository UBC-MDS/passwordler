# author: Yiwei Zhang, Michelle Hunn
# date: 2024-01-16
from passwordler.encrypt_password import encrypt_password
import pytest

def test_encrypt_password_type_error():
    """
    Test if the function returns a TypeError if the type of the input is not correct.
    """
    with pytest.raises(TypeError, match="string expected as encrypted password"):
        encrypt_password(123)

    with pytest.raises(TypeError, match="integer expected as random_seed"):
        encrypt_password("abc", random_seed="123")


def test_encrypt_password_value_error():
    """
    Test if the function returns a ValueError if the input for the encrypted_password is an emptry string.
    """
    with pytest.raises(ValueError, match="encrypted_password cannot be empty string"):
        encrypt_password('')


def test_encrypt_password_no_seed():
    """
    Test if the function returns a string as output if the seed is left as default.
    """
    result = encrypt_password('Camelot')
    assert isinstance(result, str)


def test_encrypt_normal():
    """
    Test that a standard password is correctly encrypted.
    The encrypted password should be different from the original password.
    """
    password = "testmessage"
    encrypted = encrypt_password(password, 123)
    assert encrypted != password
    assert isinstance(encrypted, str)


def test_encrypt_non_standard_characters():
    """
    Test that non-standard characters (not in the original character set) 
    are unchanged in the encrypted password.
    """
    password = "test \t\n\r\x0b\x0c"
    encrypted = encrypt_password(password, 123)
    print(encrypted)

    assert all(char in encrypted for char in " \t\n\r\x0b\x0c")
