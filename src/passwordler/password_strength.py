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
    count_special = password.count(["!", "@", "~", "#", "$", "%", '^', '&', '*', '(', ')', '?', '[', ']', '{', '}'])
    count_lowercase = len(re.findall("[a-z]", password))
    count_uppercase = password.count("[A-Z]")
    count_numeric = password.count([0-9])
    return 2