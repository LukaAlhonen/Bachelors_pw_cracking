#!/bin/python3

import sys
import bcrypt

def hash(input_file, output_file):
  with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Iterate over each line in the input file
    for line in f_in:
      # Remove any leading or trailing whitespace from the line
      line = line.rstrip('\n')

      # Generate a salt
      salt = bcrypt.gensalt()

      # Hash the password with the salt
      hashed_password = bcrypt.hashpw(line.encode('utf-8'), salt)

      # Write the hashed password to the output file in the format readable by John the Ripper
      f_out.write(f'{hashed_password.decode("utf-8")}\n')

      f_in.close()
      f_out.close()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("Usage: ./bcrypt_hash.py <input_file> <output_file>")
    sys.exit()
  hash(sys.argv[1],sys.argv[2])