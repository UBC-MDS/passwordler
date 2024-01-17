# read version from installed package
from importlib.metadata import version
# Hide internal functions in _internals.py
__all__ = ['encrypt_password', 'decrypt_password']
__version__ = version("passwordler")