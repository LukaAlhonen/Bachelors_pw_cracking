#!/bin/python3

import sys
from django.conf import settings
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password, check_password
from django.core.management.utils import get_random_secret_key

def django_to_john(hash):
    # Split the hash into its components
    components = hash.split('$')
    algorithm = components[0]
    iterations = components[1]
    salt = components[2]
    password_hash = components[3]

    # Concatenate the components in the correct order
    john_hash = f"{algorithm}${iterations}${salt}${password_hash}"

    return john_hash

def hash(input_file, output_file):
  with open(input_file, 'r') as input:
    with open(output_file, 'w') as output:
      for line in input:
        line = line.strip()
        hash = make_password(line)
        if check_password(line, hash):
          try:
            john_hash = django_to_john(hash)
            output.write(f'{john_hash}\n')
          except:
            print("hash")
            sys.exit()
  input.close()
  output.close()

def test(output_file):
  with open(output_file, 'w') as output:
    password = 'password'
    hash = make_password(password)
    output.write(f'{hash}\n')
  output.close()

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('Usage: ./django_hash.py <input_file> <output_file>')

  secret_key = get_random_secret_key()
  
  settings.configure(
  PASSWORD_HASHERS=[
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    ],
    SECRET_KEY=secret_key,
  )

  #hash(sys.argv[1], sys.argv[2])
  test(sys.argv[2])
