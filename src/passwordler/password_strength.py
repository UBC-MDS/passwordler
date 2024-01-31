import re

def password_strength(password):

    """
    Tests the strength of a password.

    This function tests the strength of a string to be used as a password. It determines password 
    strength by assessing the length and the amount of capital letters, numbers and special characters 
    used.

    Parameters:
    password (str): A string that will be tested for strength if used as a password.

    Returns:
    str: a rating of either 'weak', 'good' or 'strong'
    
    Example:
    >>> password_strength('baseball')
    Output: 'Your password is: Weak'
    >>> password_strength('Baseball4life!')
    Output: 'Your password is: Strong'
    """
    if not isinstance(password, str):
        raise TypeError("'password' should be of type 'string'")
    elif password == '':
        raise ValueError("'password' cannot be an empty string")
    
    count_uppercase = len(re.findall("[A-Z]", password))
    count_numbers = len(re.findall('[0-9]', password))
    count_special_chars = len(re.findall('[!-/:-@\\[-`{-~]', password)) 
    length = len(password)
    common_passwords = ['123456', 'password', '12345', '12345678', 'qwerty', '1234567890', '1234', 
                        'baseball', 'dragon', 'football', '1234567', 'monkey', 'letmein', 'abc123', 
                        '111111', 'mustang', 'access', 'shadow', 'master', 'michael', 'superman', 
                        '696969', '123123', 'batman', 'trustno1']

    if length >= 12 and count_uppercase >= 1 and count_numbers >= 1 and count_special_chars >= 1 and password not in common_passwords:
        return 'Your password is: Strong'
    elif length >= 8 and (count_uppercase + count_numbers + count_special_chars) >= 2 and password not in common_passwords:
        return 'Your password is: Good'
    else:
        return 'Your password is: Weak'