# passwordler

This package provides password management tools in Python. It includes four key functions, offering an integrated solution for password management with a user-friendly experience:

- **generate_password**: Creates a random password with a mix of upper and lower case letters, numbers, and symbols. The inclusion of numbers and symbols is configurable.
- **password_strength**: Assesses the strength of a string intended for use as a password by evaluating its length and the presence of capital letters, numbers, and special characters.
- **encrypt_password**: Encrypts a password using a simple substitution cipher. This function applies a character mapping based on a shuffled character set, providing basic encryption.
- **decrypt_password**: Decrypts a message that was encrypted using the `encrypt_password` function. It reverses the encryption process by mapping each character of the encrypted message back to its original character.

The `passwordler` package is ideal for users seeking comprehensive password management capabilities, from generating strong passwords to simple yet effective encryption and decryption.

## passwordler in the Python Ecosystem
While there are many password-related packages on the PyPI server, `passwordler` stands out by offering a range of password functionalities in one package. For instance, it complements functionalities found in packages like [easy-password-generator](https://pypi.org/project/easy-password-generator/) and [password-strength](https://pypi.org/project/password-strength/). While there are packages for password encryption, `passwordler` uniquely provides both encryption and decryption capabilities using a simple substitution cipher, a functionality not commonly found in existing packages.

## Installation
```
$ pip install passwordler
```

## Contributing 
Contributions to `passwordler` are welcome! For guidelines on how to contribute, please review our [Contributing document](https://github.com/UBC-MDS/passwordler/blob/main/CONTRIBUTING.md). All contributors must adhere to our [Code of Conduct](https://github.com/UBC-MDS/passwordler/blob/main/CONDUCT.md).

## License
`passwordler` is licensed under the MIT License. More information can be found [here](https://github.com/UBC-MDS/passwordler/blob/main/LICENSE).

## Credits
`passwordler` was created using [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Contributors
- Michelle Hunn 
- Kiersten Gilberg
- Rory White
- Yiwei Zhang
