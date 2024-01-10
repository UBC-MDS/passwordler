# passwordler
## Summary
This package provides password management tools in Python. The package consists of four functions. The first function is responsible for generating passwords, while the second evaluates their strength, categorizing them as weak, medium, or strong. The third function handles password encryption, ensuring data security, and the fourth function allows for decryption when necessary. 

## List of functions
password_creator
password_strength
password_encryption
password_decryption

## How does the package fit in the Python ecosystem?
There are multiple packages that generate passwords, which is the same as our password_creator. These packages can be found [here](https://pypi.org/search/?q=password+generator&o=). There are also other packages that check for the strength of passwords, an example can be seen [here](https://pypi.org/project/password-strength/), this is the same as our password_strength function. There is also a [password encryption package](https://pypi.org/project/password/) which does the same thing as our password_encryption functions. However, there were no password decryption specific function on PyPI. The benefit of our package is that it provides a range of password related functions. 