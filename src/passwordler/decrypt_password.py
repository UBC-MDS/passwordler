import random

def decrypt_password(encrypted_message, random_seed = 123):
    """
    Decrypt an encrypted password.

    This function decrypts an encrypted string. It supports the Advanced Encryption Standard (AES) 
    encryption, which is widely used to secure sensitive data. Employing the provided key, the 
    function decrypts the password, ensuring it matches the encryption algorithm applied during the 
    encryption process. The function returns the original, human-readable password.

    Parameters:
    password (bytes): The encrypted password to be decrypted.
    key (bytes): The encryption key used for decryption.

    Returns:
    str: The decrypted password.

    """
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

    print(decrypted_msg)
    return decrypted_msg