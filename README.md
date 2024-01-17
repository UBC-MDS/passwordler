# passwordler

This package provides password management tools in Python. The package consists of four functions:
- **generate_password**: This function creates a random password containing a mix of upper and lower case letters, numbers, and symbols. The inclusion of numbers and symbols can be controlled through parameters.
- **password_strength**: This function tests the strength of a string to be used as a password. It determines password strength by assessing the length and the amount of capital letters, numbers and special characters used.
- **encrypt_password**: Encrypts a password using a simple substitution cipher. This function applies a character mapping based on a shuffled character set, providing basic encryption.
- **decrypt_password**: Decrypts a message that was encrypted using the `encrypt_password` function. It reverses the encryption process by mapping each character of the encrypted message back to its original character.

This Python package is useful for users seeking an integrated solution for password management, offering a user-friendly experience. With key functionalities consolidated in one package, users can effortlessly generate strong passwords, evaluate their strength, and grasp encryption and decryption methods through our straightforward substitution cipher.

## passwordler in the Python Ecosystem
There are many password related packages already on the PyPI server. We have selected a few key examples that complete the same functions as our package. An example of a package that is similar to our password_creator function can be found [here](https://pypi.org/project/easy-password-generator/). Similarly, there are also other packages that check for the strength of passwords, one of which can be seen [here](https://pypi.org/project/password-strength/), this is similar to our password_strength function. There is also a [password encryption package](https://pypi.org/project/password/) which does the same thing as our password_encryption functions. However, there were no password decryption specific function on PyPI. The advantage of our package lies in its comprehensive suite of password-related functions, complemented by an original and intuitive algorithm that demonstrates the fundamental principles of password encryption and decryption.

## Installation
```
$ pip install passwordler
```

## Contributing 
For information about how to contribute to this package, please review our [Contributing document](https://github.com/UBC-MDS/passwordler/blob/main/CONTRIBUTING.md). All contributors must abide by our [Code of Conduct](https://github.com/UBC-MDS/passwordler/blob/main/CONDUCT.md)

## License
This packages uses the MIT License, more information can be found [here](https://github.com/UBC-MDS/passwordler/blob/main/LICENSE)


## Credits
`passwordler` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter)

## Contributors
- Michelle Hunn
- Kiersten Gilberg
- Rory White
- Yiwei Zhang