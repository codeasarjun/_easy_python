
This directory contains examples and practices for improving security in Python applications.

## Files

### `password_hashing.py`
This script demonstrates how to hash passwords using bcrypt and how to verify them. Hashing passwords is crucial for protecting user credentials.

#### Usage
To hash a password:
```python
from password_hashing import hash_password

hashed_password = hash_password("your_password")
print(hashed_password)
```


# secure_coding_practices.py

This script provides examples of secure coding practices, including input validation and sanitization. Proper input handling is essential to prevent common security vulnerabilities such as SQL injection, cross-site scripting (XSS), and other types of attacks.

## Usage

### To validate an email address:

```python
import re
def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```