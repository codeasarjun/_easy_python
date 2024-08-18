import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def sanitize_input(user_input: str) -> str:
    """sanitize input to prevent injection attacks."""
    return re.sub(r'[^\w\s]', '', user_input)

if __name__ == "__main__":
    email = "test@example.com"
    print(f"Is valid email: {is_valid_email(email)}")

    user_input = "DROP TABLE users; --"
    sanitized = sanitize_input(user_input)
    print(f"Sanitized input: {sanitized}")
