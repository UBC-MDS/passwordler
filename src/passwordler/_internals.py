# author: Michelle Hunn, Yiwei Zhang
# date: 2024-01-16
import string

accented_chars = ['á', 'à', 'â', 'ä', 'ã', 'å', 'æ', 'ç', 'é', 'è', 'ê', 'ë', 'í',
                  'ì', 'î', 'ï', 'ñ', 'ó', 'ò', 'ô', 'ö', 'õ', 'ø', 'œ', 'ú', 'ù', 'û', 'ü', 'ý', 'ÿ']
string_builtin_chars = string.ascii_letters + string.digits + string.punctuation

# Combine the lists
original = accented_chars + list(string_builtin_chars)

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