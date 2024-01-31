import random
from ._internals import original, getKeyMap

def decrypt_password(encrypted_message, random_seed = 123):
    """
    Decrypt an encrypted password or message using a simple substitution cipher.
    
    The function uses a substitution cipher to decrypt an encrypted string. The 
    original set is replaced with a randomly shuffled character from the same set.
    The random seed is utilized to make sure that the encryption and the decryption 
    matches.   

    Parameters:
    - encrypted_message (str): The encrypted message to be decrypted.
    - random_seed (int): Seed for the random number generator to ensure that 
                         encryption and decryption match. Default is 123.

    Returns:
    - str: The decrypted message.

    The function uses a substitution cipher where each character in the original
    set is replaced with a randomly shuffled character from the same set. The random
    seed is utilized to maintain consistent decryption results when needed.

    Example:
    >>> original_message = 'Monty Python'
    >>> encrypted_message = encrypt_password(original_message, random_seed = 123)
    >>> decrypted_message = decrypt_password(encrypted_message, random_seed = 123)
    Output: 'Monty Python'
    """
    if not isinstance(encrypted_message, str):
        raise TypeError(
            f"string expected as encrypted message, got '{type(encrypted_message)}'"
            )
    
    if not isinstance(random_seed, int):
        raise TypeError(
            f"integer expected as random_seed, got '{type(random_seed)}'"
            )
    
    if encrypted_message == '':
        raise ValueError(
            'encrypted_message cannot be empty string')
    
    random.seed(random_seed)

    decryption = original.copy()
    random.shuffle(decryption)

    keyMap = getKeyMap(decryption, isDecryption=True)
    decrypted_msg = []

    for character in encrypted_message:
        if character in keyMap:
            decrypted_msg.append(keyMap[character])
        else:
            decrypted_msg.append(character)

    decrypted_msg = ''.join(decrypted_msg)

    return decrypted_msg