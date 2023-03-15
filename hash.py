#!/bin/python3

import hashlib
import sys

def hash(input_file_path, output_file_path, hash):
    with open(input_file_path, 'r') as input_file:
        with open(output_file_path, 'w') as output_file:
            for line in input_file:
                line = line.strip()  # Remove newline character
                #hash_value = hashlib.md5(line.encode('utf-8')).hexdigest()  # Generate md5 hash
                hash_value = getattr(hashlib,hash)(line.encode('utf-8')).hexdigest()
                output_file.write(f"{hash_value}\n")  # Write to output file in John the Ripper format
    input_file.close()
    output_file.close()

if __name__ == '__main__':
  if len(sys.argv) != 4:
      print("Usage: ./hash.py <input_file> <output_file>")
      sys.exit()
  hash(sys.argv[1],sys.argv[2],sys.argv[3])