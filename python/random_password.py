import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

password_length = 20

def generate_password():
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    return "".join(password)
    
    