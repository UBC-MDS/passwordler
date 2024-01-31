import random
import string

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
    
    Example:
    >>> generate_password()
    Output: ',tKC]m"wDJ34'
    >>> generate_password(include_symbols=False, include_numbers=False)
    Output: 'NJfVKhgnrJYa'
    """

    if not isinstance(length, int):
        raise TypeError("Length must be an integer.")
    
    if length < 12 or length > 100:
        raise ValueError("Password length must be between 12 and 100 characters.")

    if not isinstance(include_symbols, bool):
        raise TypeError("include_symbols must be a boolean value.")
    
    if not isinstance(include_numbers, bool):
        raise TypeError("include_numbers must be a boolean value.")
   
    # Ensure that the password contains at least one of each type of character specified
    password_characters = [random.choice(string.ascii_uppercase), random.choice(string.ascii_lowercase)]
    if include_numbers:
        password_characters.append(random.choice(string.digits))
    if include_symbols:
        password_characters.append(random.choice(string.punctuation))

    # Generate master list of characters to choose from
    possible_chars = string.ascii_letters
    if include_numbers:
        possible_chars += string.digits
    if include_symbols:
        possible_chars += string.punctuation

    # Fill the rest of the password length with random characters from the possible set
    password_characters.extend(random.choice(possible_chars) for _ in range(length - len(password_characters)))

    random.shuffle(password_characters)

    final_password = ''.join(password_characters)
    return final_password