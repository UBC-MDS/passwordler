import random

original = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
            'Z', 'é', 'è', 'à', 'ü', 'ö', 'ä', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '.', ',', ';', ':', '!', '?', '+', '@', '#', '%', '&', '$', '£', '=', '-', '_', ' ',]


def getKeyMap(shuffled, isDecryption=False):
    """
    Generate a key map for encryption or decryption.

    This function creates a mapping between characters of the original character set and a shuffled 
    version. It can be used for both encryption and decryption depending on the 'isReverse' flag.

    Parameters:
    shuffled (list): The shuffled list of characters.
    isReverse (bool): Flag to indicate if the mapping is for decryption (True) or encryption (False).

    Returns:
    dict: A dictionary mapping each character of the original set to the shuffled set or vice versa.
    """
    keyMap = {}
    for i in range(len(shuffled)):
        if isDecryption:  # For decryption
            keyMap[shuffled[i]] = original[i]
        else:  # For encryption
            keyMap[original[i]] = shuffled[i]
    return keyMap


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
