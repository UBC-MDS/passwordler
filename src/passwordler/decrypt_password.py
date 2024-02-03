import random
from ._internals import original, getKeyMap

def decrypt_password(encrypted_password, random_seed = 123):
    """
    Decrypt an encrypted password using a simple substitution cipher.
    
    The function uses a substitution cipher to decrypt an encrypted string. The 
    original set is replaced with a randomly shuffled character from the same set.
    The random seed is utilized to make sure that the encryption and the decryption 
    matches.   

    Parameters:
    - encrypted_password (str): The encrypted password to be decrypted.
    - random_seed (int): Seed for the random number generator to ensure that 
                         encryption and decryption match. Default is 123.

    Returns:
    - str: The decrypted password.

    The function uses a substitution cipher where each character in the original
    set is replaced with a randomly shuffled character from the same set. The random
    seed is utilized to maintain consistent decryption results when needed.

    Example:
    >>> original_password = 'Monty Python'
    >>> encrypted_password = encrypt_password(original_password, random_seed = 123)
    >>> decrypted_password = decrypt_password(encrypted_password, random_seed = 123)
    Output: 'Monty Python'
    """
    if not isinstance(encrypted_password, str):
        raise TypeError(
            f"string expected as encrypted password, got '{type(encrypted_password)}'"
            )
    
    if not isinstance(random_seed, int):
        raise TypeError(
            f"integer expected as random_seed, got '{type(random_seed)}'"
            )
    
    if encrypted_password == '':
        raise ValueError(
            'encrypted_password cannot be empty string')
    
    random.seed(random_seed)

    decryption = original.copy()
    random.shuffle(decryption)

    # generate a key map for decryption
    keyMap = getKeyMap(decryption, isDecryption=True)
    decrypted_pass = []

    # decrypt password with key map
    for character in encrypted_password:
        if character in keyMap:
            decrypted_pass.append(keyMap[character])
        else:
            decrypted_pass.append(character)

    decrypted_pass = ''.join(decrypted_pass)

    return decrypted_pass