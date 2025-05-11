import string
import random

def generate_password(length=12, include_numbers=True, include_special_chars=True, include_uppercase=True):
    
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase

    return ''.join(random.choice(characters) for _ in range(length))