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


def decrypt_password(encrypted_message, random_seed=123):
    """
    Decrypt a message encrypted with the simple substitution cipher.

    This function decrypts a given message by mapping each character back to its original character
    using the same shuffled character set used for encryption. The function requires the same random
    seed that was used for encryption to ensure consistent shuffling.

    Parameters:
    encrypted_message (str): The message to be decrypted.
    random_seed (int): The seed used for random shuffling (should be the same as used in encryption).

    Returns:
    str: The decrypted message.
    """
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
