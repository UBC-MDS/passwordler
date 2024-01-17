import random

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
    >>> encrypted = encrypt_password('Monty Python', random_seed = 123)
    >>> decrypted = decrypt_password(encrypted, random_seed = 123)
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
    
    random.seed(random_seed)
    
    original = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                'r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H',
                'I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y',
                'Z','é','è','à','ü','ö','ä','0','1','2','3','4','5','6','7','8','9',
                '.',',',';',':','!','?','+','@','#','%','&','$','£','=','-','_',' ',]

    encryption = original.copy()
    random.shuffle(encryption)
    
    decrypted_msg = []

    for character in encrypted_message:
        if character in original:
            index = encryption.index(character)
            new_char = original[index]
            decrypted_msg.append(new_char)
        else:
            decrypted_msg.append(character)

    decrypted_msg = ''.join(decrypted_msg)

    return decrypted_msg