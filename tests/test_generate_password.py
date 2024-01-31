from passwordler.generate_password import generate_password
from passwordler.password_strength import password_strength
import pytest

def test_generate_password_type_error():
    """
    Test if the function returns a TypeError if the type of the input is not correct.
    """
    with pytest.raises(TypeError, match="Length must be an integer."):
        generate_password("abc")

def test_generate_password_value_error():
    """
    Test if the function returns a ValueError if the value of the input is not correct.
    """
    with pytest.raises(ValueError, match="Password length must be between 12 and 100 characters."):
        generate_password(1)

def test_generate_password_include_symbols_type_error():
    """
    Test if the function returns a TypeError if the type of the input is not correct.
    """
    with pytest.raises(TypeError, match="include_symbols must be a boolean value."):
        generate_password(12, include_symbols="abc")

def test_generate_password_include_numbers_type_error():
    """
    Test if the function returns a TypeError if the type of the input is not correct.
    """
    with pytest.raises(TypeError, match="include_numbers must be a boolean value."):
        generate_password(12, include_numbers="abc")

def test_generate_password_length():
    """
    Test if the length of the generated password is correct.
    """
    assert len(generate_password(12)) == 12
    assert len(generate_password(100)) == 100

def test_generate_password_include_symbols():
    """
    Test if the generated password includes symbols.
    """
    assert any(char in generate_password(12, include_symbols=True) for char in "!@#$%^&*()")

def test_generate_password_include_numbers():
    """
    Test if the generated password includes numbers.
    """
    ret = generate_password(12, include_numbers=True)
    assert any(char in ret for char in "0123456789")
    
def test_generate_password_strength():
    """
    Test if the generated password has the correct strength.
    """
    assert password_strength(generate_password(12)) == "Your password is: Strong"