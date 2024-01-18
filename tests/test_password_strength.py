import pytest
from passwordler.password_strength import password_strength

def test_empty_string():
    """Check ValueError is raised when given empty string"""
    with pytest.raises(ValueError):
        empty_string = ""
        password_strength(empty_string)

def test_non_string():
    """Check TypeError is raised when given a non-string value"""
    with pytest.raises(TypeError):
        non_string = 1234
        password_strength(non_string)

def test_strong():
    """Check that function returns strong when length is 12 characters, one number, one capital, one 
    special character"""
    expected = 'Your password is: Strong'
    actual = password_strength('Strongpass1!')
    assert actual == expected, 'Length 12 with number, capital and special character categorized incorrectly'

def test_good_capnum():
    """Check that function returns good when length 8 characters, one capital, one number """
    expected = 'Your password is: Good'
    actual = password_strength('Eightpa1')
    assert actual == expected, 'Length 8 with one capital, one number categorized incorrectly' 

def test_good_capspecial():
    """Check that function returns good when length 8 characters, one capital, one special character """
    expected = 'Your password is: Good'
    actual = password_strength('Eightpa!')
    assert actual == expected, 'Length 8 with one capital, one special character categorized incorrectly'

def test_good_numspecial():
    """Check that function returns good when length 8 characters, one number, one special character """
    expected = 'Your password is: Good'
    actual = password_strength('8ightpa!')
    assert actual == expected, 'Length 8 with one number, one special character categorized incorrectly'

def test_weak():
    """Check that function returns weak when length < 8 characters"""
    expected = 'Your password is: Weak'
    actual = password_strength('Eight!8')
    assert actual == expected, 'Length less than 8 categorized incorrectly'

def test_commonpass():
    """Check that function returns weak when a common password is used"""
    expected = 'Your password is: Weak'
    actual = password_strength('football')
    assert actual == expected, 'Common password categorized incorrectly'

def test_nonenglish_char():
    """Check that function treats characters from other languages as lowercase english characters"""
    expected = 'Your password is: Weak'
    actual = password_strength('Ёeakpassword1')
    assert actual == expected, 'Non-english letters categorized incorrectly'