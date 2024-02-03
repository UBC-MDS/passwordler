# author: Michelle Hunn, Yiwei Zhang
# date: 2024-01-16
import random
from ._internals import original, getKeyMap

def encrypt_password(password, random_seed=123):
    """
    Encrypt a password using a simple substitution cipher.

    This function encrypts a password by substituting each character with a corresponding character 
    from a shuffled set, using the same set of characters as the decryption function. The shuffle 
    is controlled by a random seed to ensure reproducible results, allowing encrypted passwords 
    to be consistently decrypted using the matching seed. Characters not included in the 
    substitution set remain unchanged in the encrypted password.

    Parameters:
    - password (str): The password to be encrypted.
    - random_seed (int): Seed for the random number generator to ensure consistent encryption 
                         results. Default value is 123.

    Returns:
    - str: The encrypted password.

    Example:
    >>> original_password = 'Monty Python'
    >>> encrypted_password = encrypt_password(original_password, random_seed = 123)
    >>> decrypted_password = decrypt_password(encrypted_password, random_seed = 123)
    Output: 'Monty Python'
    """
    if not isinstance(password, str):
        raise TypeError(
            f"string expected as encrypted password, got '{type(password)}'"
        )

    if not isinstance(random_seed, int):
        raise TypeError(
            f"integer expected as random_seed, got '{type(random_seed)}'"
        )

    if password == '':
        raise ValueError(
            'encrypted_password cannot be empty string')

    random.seed(random_seed)

    encryption = original.copy()
    random.shuffle(encryption)

    # generate a key map for encryption
    keyMap = getKeyMap(encryption)
    encrypted_pass = []

    # encrypt password with key map
    for character in password:
        if character in original:
            encrypted_pass.append(keyMap[character])
        else:
            encrypted_pass.append(character)

    encrypted_pass = ''.join(encrypted_pass)

    return encrypted_pass
