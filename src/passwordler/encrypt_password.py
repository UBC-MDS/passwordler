# author: Michelle Hunn, Yiwei Zhang
# date: 2024-01-16
import random
from ._internals import original, getKeyMap

def encrypt_password(message, random_seed=123):
    """
    Encrypt a message using a simple substitution cipher.

    This function encrypts a message by substituting each character with a corresponding character 
    from a shuffled set, using the same set of characters as the decryption function. The shuffle 
    is controlled by a random seed to ensure reproducible results, allowing encrypted messages 
    to be consistently decrypted using the matching seed. Characters not included in the 
    substitution set remain unchanged in the encrypted message.

    Parameters:
    - message (str): The message to be encrypted.
    - random_seed (int): Seed for the random number generator to ensure consistent encryption 
                         results. Default value is 123.

    Returns:
    - str: The encrypted message.

    Example:
    >>> original_message = 'Monty Python'
    >>> encrypted_message = encrypt_password(original_message, random_seed = 123)
    >>> decrypted_message = decrypt_password(encrypted_message, random_seed = 123)
    Output: 'Monty Python'
    """
    if not isinstance(message, str):
        raise TypeError(
            f"string expected as encrypted message, got '{type(message)}'"
        )

    if not isinstance(random_seed, int):
        raise TypeError(
            f"integer expected as random_seed, got '{type(random_seed)}'"
        )

    if message == '':
        raise ValueError(
            'encrypted_message cannot be empty string')

    random.seed(random_seed)

    encryption = original.copy()
    random.shuffle(encryption)

    keyMap = getKeyMap(encryption)
    encrypted_msg = []

    for character in message:
        if character in original:
            encrypted_msg.append(keyMap[character])
        else:
            encrypted_msg.append(character)

    encrypted_msg = ''.join(encrypted_msg)

    return encrypted_msg
