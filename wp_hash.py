import hashlib
import bcrypt
from wordpress import wp_hash_password

def hash_passwords(filename):
    with open(filename, 'r') as f:
        passwords = [line.strip() for line in f.readlines()]
    
    hashed_passwords = []
    for password in passwords:
        hashed_password = wp_hash_password(password)
        hashed_passwords.append(hashed_password)
        
    return hashed_passwords
