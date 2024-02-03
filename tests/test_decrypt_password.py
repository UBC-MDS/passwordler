import pytest
import random
from passwordler.decrypt_password import decrypt_password


def test_decrypt_password_type_error():
    """
    Test if the function returns a TypeError if the type of the input is not correct.
    """
    with pytest.raises(TypeError, match="string expected for encrypted password"):
        decrypt_password(123)

    with pytest.raises(TypeError, match="integer expected as random_seed"):
        decrypt_password("abc", random_seed="123")


def test_decrypt_password_value_error():
    """
    Test if the function returns a ValueError if the input for the argument encrypted_password is an empty string.
    """
    with pytest.raises(ValueError, match="encrypted_password argument cannot be empty string"):
        decrypt_password("")


def test_decrypt_password_no_seed():
    """
    Test if the function returns a string as output if the seed is left as default.
    """
    result = decrypt_password("Camelot")
    assert isinstance(result, str)


def test_decrypt_password_upper_vs_lower_case():
    """
    Test that the function handles case sensitivity correctly.
    """
    result_lower = decrypt_password("spam", random_seed=42)
    result_upper = decrypt_password("SPAM", random_seed=42)
    assert result_lower != result_upper


def test_decrypt_password_special_characters_input():
    """
    Test if the function handles special characters correctly.
    """
    result = decrypt_password("@#$%^&*()_+=-]|;:,.<>?/`~", random_seed=42)
    assert isinstance(result, str)


def test_decrypt_password_long_input_password():
    """
    Test if the function handles longer passwords correctly.
    """
    result = decrypt_password(
        "I say you are, and I should know. I followed a few!", random_seed=42
    )
    assert isinstance(result, str)
