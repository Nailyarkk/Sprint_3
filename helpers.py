import random
import string

def generate_random_login():
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    domain = random.choice(['gmail.com', 'list.ru', 'outlook.com'])
    return f"{username}@{domain}"

def generate_random_password(length=12, include_special_chars=True):
    chars = string.ascii_letters + string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_random_name(length=8):
    letters = string.ascii_letters
    name = ''.join(random.choice(letters) for _ in range(length))
    return name
