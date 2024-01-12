# passwordler

This package provides password management tools in Python. The package consists of four functions. The first function is responsible for generating passwords, while the second evaluates their strength, categorizing them as weak, good, or strong. The third function handles password encryption, ensuring data security, and the fourth function allows for decryption when necessary. 

Functions included in this package:
- generate_password: This function creates a random password containing a mix of upper and lower case letters, numbers, and symbols. The inclusion of numbers and symbols can be controlled through parameters.
- password_strength: This function tests the strength of a string to be used as a password. It determines password strength by assessing the length and the amount of capital letters, numbers and special characters used.
- encrypt_password: This function encrypts a password using a specified encryption algorithm and key. Currently, it supports AES encryption. The function applies padding to the password to match the block size requirement of the encryption algorithm.
- decrypt_password: This function decrypts an encrypted string. It supports the Advanced Encryption Standard (AES) encryption, which is widely used to secure sensitive data. Employing the provided key, the function decrypts the password, ensuring it matches the encryption algorithm applied during the encryption process. The function returns the original, human-readable password.


There are many password related packages already on the PyPI server. We have selected a few key examples that complete the same functions as our package. An example of a package that is similar to our password_creator function can be found [here](https://pypi.org/project/easy-password-generator/). Similarly, there are also other packages that check for the strength of passwords, one of which can be seen [here](https://pypi.org/project/password-strength/), this is similar to our password_strength function. There is also a [password encryption package](https://pypi.org/project/password/) which does the same thing as our password_encryption functions. However, there were no password decryption specific function on PyPI. The benefit of our package is that it provides a range of password related functions. 

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