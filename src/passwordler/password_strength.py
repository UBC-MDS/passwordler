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
    """
    count_uppercase = len(re.findall("[A-Z]", password))
    count_numbers = len(re.findall('[0-9]', password))
    count_special_chars = len(re.findall('[!-\/:-@[-`{-~]', password)) 
    length = len(password)

    if length >= 12 and count_uppercase >= 1 and count_numbers >= 1 and count_special_chars >= 1:
        return 'Your password is: Strong'
    elif length >= 8 and (count_uppercase + count_numbers + count_special_chars) > 2:
        return 'Your password is: Good'
    else:
        return 'Your password is: Weak'