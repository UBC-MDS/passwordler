import pytest
from passwordler.decrypt_password import decrypt_password
from passwordler.encrypt_password import encrypt_password

def test_decrypt_password_type_error():
    with pytest.raises(TypeError, match="string expected as encrypted message"):
        decrypt_password(123)

    with pytest.raises(TypeError, match="integer expected as random_seed"):
        decrypt_password("abc", random_seed="123")

def test_decrypt_password_value_error():
    with pytest.raises(ValueError, match="encrypted_message cannot be empty string"):
        decrypt_password('')

def test_decrypt_password_no_seed():
    result = decrypt_password('Camelot')
    assert isinstance(result, str)

def test_decrypt_password_upper_vs_lower_case():
    result_lower = decrypt_password('spam', random_seed=42)
    result_upper = decrypt_password('SPAM', random_seed=42)
    assert result_lower != result_upper

def test_decrypt_password_special_characters_input():
    result = decrypt_password('@#$%^&*()_+=-]|;:,.<>?/`~', random_seed=42)
    assert isinstance(result, str)

def test_decrypt_password_long_input_message():
    result = decrypt_password('I say you are, and I should know. I followed a few!.', random_seed=42)
    assert isinstance(result, str)

"""
def test_encryption_decryption():
     encrypted_message = encrypt_password('Monty Python', random_seed=123)

    assert (
        decrypt_password(encrypted_message, random_seed=123) == "Monty Python"
    ), "The encrypted message is not the same as the initial message"
"""