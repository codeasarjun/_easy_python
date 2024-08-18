import hashlib
import os

def hash_password(password: str) -> str:
    salt = os.urandom(16)
    dk = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, 100000)
    return salt + dk

def verify_password(stored_hash: bytes, password: str) -> bool:
    salt = stored_hash[:16]
    stored_key = stored_hash[16:]
    dk = hashlib.pbkdf2_hmac('sha512', password.encode(), salt, 100000)
    return stored_key == dk

if __name__ == "__main__":
    password = "supersecret"
    hashed_password = hash_password(password)
    print(f"Hashed Password: {hashed_password}")

    is_correct = verify_password(hashed_password, password)
    print(f"Password Match: {is_correct}")