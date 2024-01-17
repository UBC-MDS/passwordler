# author: Michelle Hunn, Yiwei Zhang
# date: 2024-01-16
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