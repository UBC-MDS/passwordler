import pytest
import random
from passwordler.decrypt_password import decrypt_password
from passwordler.encrypt_password import encrypt_password


def test_encryption_decryption():
    """
    Test if the encryption and decryption function match each other.
    """
    encrypted_message = encrypt_password("Monty Python", random_seed=123)

    assert (
        decrypt_password(encrypted_message, random_seed=123) == "Monty Python"
    ), "The encrypted message is not the same as the initial message"
