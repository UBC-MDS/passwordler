# passwordler

<img src="https://github.com/UBC-MDS/passwordler/assets/125914446/1648cb38-c2b7-4cd8-9dc3-c57077d4d520" width="150">


[![Documentation Status](https://readthedocs.org/projects/passwordler/badge/?version=latest)](https://passwordler.readthedocs.io/en/latest/?badge=latest) [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-360/) ![ci-cd](https://github.com/UBC-MDS/passwordler/actions/workflows/ci-cd.yml/badge.svg) [![codecov](https://codecov.io/gh/UBC-MDS/passwordler/branch/main/graph/badge.svg)](https://codecov.io/gh/UBC-MDS/passwordler)


This package provides password management tools in Python. The package consists of four functions:
- `generate_password`:
   - This function creates a random password containing a mix of upper and lower-case letters, numbers, and symbols. The inclusion of numbers and symbols can be controlled through parameters.
- `password_strength`:
   - This function tests the strength of a string to be used as a password. It determines password strength by assessing the length and the amount of capital letters, numbers and special characters used.
- `encrypt_password`:
   - Encrypts a password using a simple substitution cipher. This function applies a character mapping based on a shuffled character set, providing basic encryption.
- `decrypt_password`:
   - Decrypts a message that was encrypted using the `encrypt_password` function. It reverses the encryption process by mapping each character of the encrypted message back to its original character.

This Python package is useful for users seeking an integrated solution for password management, offering a user-friendly experience. With key functionalities consolidated in one package, users can effortlessly generate strong passwords, evaluate their strength, and grasp encryption and decryption methods through our straightforward substitution cipher.

## passwordler in the Python Ecosystem

There are many password related packages already on the PyPI server. We have selected a few key examples that complete the same functions as our package. An example of a package that is similar to our password_creator function can be found [here](https://pypi.org/project/easy-password-generator/). Similarly, there are also other packages that check for the strength of passwords, one of which can be seen [here](https://pypi.org/project/password-strength/), this is similar to our password_strength function. There is also a [password encryption package](https://pypi.org/project/password/) which does the same thing as our password_encryption functions. However, there were no password decryption specific function on PyPI. The advantage of our package lies in its comprehensive suite of password-related functions, complemented by an original and intuitive algorithm that demonstrates the fundamental principles of password encryption and decryption.

## Unique Features of passwordler

`passwordler` stands out in the realm of password management packages due to its unique blend of user-friendliness and security, tailored for individuals with varying levels of technical expertise. Here's what sets `passwordler` apart:

1. **Ease of Understanding**:
   - Every aspect of the encryption and decryption process is designed to be easily understood, even by users with only high-school-level tech knowledge.
  
2. **Simplicity Over Complexity**:
   - The package avoids the complexity and opacity of nested package dependencies. It is not simply importing and adjusting the parameters of industry-standard AES encryption or SHA-256 hashing, but trying to make the workflow as transparent as possible.

3. **Enhanced Security for Beginners**:
   - Unlike naive encryption techniques like the Caesar Cipher and Vigenere Cipher, which are educational but also easy to crack with a finite number of guesses, `passwordler` provides a level of security that surpasses beginner-level algorithms.

4. **Original Algorithm**:
   - The encryption algorithm was developed from the ground up, maintaining originality and individual intellectual property.

`passwordler` is perfect for users who want to understand and control their password security without delving into complex cryptographic standards. It offers more security than basic algorithms, all while ensuring the codebase remains accessible and maintainable.

## Installation

To install `passwordler` type the following command into your terminal:
```
$ pip install passwordler
```

## Documentation

Our online documentation can be found [here](https://passwordler.readthedocs.io/en/latest/?badge=latest).

## Using `passwordler` in Python

After installing `passwordler` with pip, you can use its functions in Python as follows:

1. **Encrypting a Password**:

   ```python
   from passwordler.encrypt_password import encrypt_password

   # Encrypt a password with a default seed
   encrypted_password = encrypt_password("YourPasswordHere")
   print(encrypted_password)  # Prints the encrypted password
   ```

   If you want to use a specific seed for the encryption, you can pass it as a second argument:

   ```python
   # Encrypt a password with a specific seed
   encrypted_password = encrypt_password("YourPasswordHere", 42)
   print(encrypted_password)  # Prints the encrypted password using the specified seed
   ```

2. **Decrypting a Password**:

   To decrypt a password that was encrypted with the `encrypt_password` function, use the `decrypt_password` function with the same seed used for encryption:

   ```python
   from passwordler.decrypt_password import decrypt_password

   # Decrypt a password
   decrypted_password = decrypt_password(encrypted_password, 42)
   print(decrypted_password)  # Prints the decrypted password, which should match "YourPasswordHere"
   ```

3. **Evaluating Password Strength**:

   The `password_strength` function evaluates the strength of a password based on length, use of uppercase letters, numbers, and special characters:

   ```python
   from passwordler.password_strength import password_strength

   # Evaluate the strength of a password
   strength = password_strength("YourPasswordHere")
   print(strength)  # Prints the strength of the password (e.g., 'Your password is: Strong')
   ```

   Remember to replace `"YourPasswordHere"` with the actual password you wish to process in the above examples. The `password_strength` function will rate the password as 'Weak', 'Good', or 'Strong' based on its complexity and common password patterns.

4. **Generating a Password**:

   `generate_password` allows you to create a secure password of customizable length and complexity, with options to include or exclude special characters and numbers.
   
   ```python
   from passwordler.generate_password import generate_password
   # Encrypt a password with a default seed
   password = generate_password()
   print(password)  # Prints the generated password
   ```
   
   The function has three default parameters: `length`=12, `include_special_characters`=True, `include_numbers`=True. You can change these parameters to generate a password of your liking.
   
   ```python
        generate_password(45, False, False)  # Generates a password of length 45 without special characters and numbers
   ```

### Running Tests
 
To ensure `passwordler` is functioning correctly on your system, you can run the test suite with `pytest`. First, ensure you have `pytest` installed:

```bash
$ pip install pytest
```

If you have cloned the repository and want to run the tests, navigate to the root directory of the project and execute:

```bash
$ pytest
```

To show test coverage report
```bash
$ pytest --cov=passwordler --cov-report term
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
