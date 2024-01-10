def generate_password(length=12, include_symbols=True, include_numbers=True):
    """
    Generate a password.

    This function creates a random password containing a mix of upper and lower case letters, 
    numbers, and symbols. The inclusion of numbers and symbols can be controlled through parameters.

    Parameters:
    length (int): The length of the password to be generated. Default is 12 characters.
    include_symbols (bool): Whether to include symbols in the password. Default is True.
    include_numbers (bool): Whether to include numbers in the password. Default is True.

    Returns:
    str: A randomly generated password.
    """