def encrypt_password(raw_password: str, encrypt_algo: list = ['AES']) -> str:
    """
    Encrypt a given password.

    This function encrypts a password using a specified encryption algorithm. Currently, it supports AES encryption.
    The function applies padding to the password to match the block size requirement of the encryption algorithm.

    Parameters:
    raw_password (str): The password to be encrypted.
    encrypt_algo (list): List of encryption algorithms to use. Default is ['AES'].

    Returns:
    str: The encrypted password.
    """