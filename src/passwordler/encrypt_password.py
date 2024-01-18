# author: Michelle Hunn, Yiwei Zhang
# date: 2024-01-16
import random
from ._internals import original, getKeyMap

def encrypt_password(message, random_seed=123):
    """
    Encrypt a message using a simple substitution cipher.

    This function encrypts a given message by mapping each character to a corresponding character 
    in a shuffled character set. The function uses a predefined list of characters and a random 
    seed to ensure consistent shuffling. Characters not in the predefined list remain unchanged.

    Parameters:
    message (str): The message to be encrypted.
    random_seed (int): The seed used for random shuffling (default is 123).

    Returns:
    str: The encrypted message.
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
