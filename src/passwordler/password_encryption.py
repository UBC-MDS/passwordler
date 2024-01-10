from Crypto.Cipher import AES
import os

def password_encryption(raw_password: str, encrypt_algo: list = ['AES']) -> str:
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

    # Define block size and padding function for AES
    BS = AES.block_size
    pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

    # Only AES is implemented, for now, raise error for other algorithms
    if 'AES' not in encrypt_algo or len(encrypt_algo) > 1:
        raise NotImplementedError("Currently, only AES encryption is implemented.")

    # Generate a random key for AES encryption
    key = os.urandom(32)  # AES requires a key of 16, 24, or 32 bytes

    # Encrypt the password
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_password = cipher.encrypt(pad(raw_password))

    # Returning the encrypted password as a hexadecimal string for readability
    return encrypted_password.hex()
