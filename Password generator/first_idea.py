"""
Mega genius strong password generator
"""

import hashlib
import os
import sys

def generate(plaintext):
    hash = hashlib.sha1(plaintext.encode()).hexdigest()
    return hash[12:28]

if not len(sys.argv) == 2:
    print("Incorrect use")
    sys.exit(1)
else:
    password = sys.argv[1]
    strong_password = generate(password)
    print(f"Your strong password: {strong_password}")
