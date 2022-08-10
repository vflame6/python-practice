"""
Strong password generator

Usage: python3 pgenerator.py plaintext
Or you can import it's class Generator
"""

import argparse
import hashlib
from pydoc import plain
import re
import requests

class Generator(object):
    def __init__(self):
        # Minimal strong password length
        self.min_length = 12

    def __repr__(self):
        return "Generator()"

    def generate_symbol(self, c: str, offset: int) -> str:
        return chr(((ord(c) + offset) * 69) % 256)

    def generate(self, plaintext: str) -> str:
        result = ""
        ln = len(plaintext)

        while len(result) < self.min_length:
            for symbol in plaintext:
                c = self.generate_symbol(symbol, 0)
                ofs = 0

                while not re.findall("[a-zA-Z0-9!\*@%]", c):
                    ofs += 1
                    c = self.generate_symbol(c, ofs)
                result += c
        return result

    def check_password(self, plaintext: str) -> int:
        """
        Converts a plaintext string into SHA-1 hash and then verifies if it has ever been cracked by Have I Been Pwned API.
        """

        hash = hashlib.sha1(plaintext.encode())
        hash = hash.hexdigest()
        first_five = hash[:5]
        last_part = hash[5:].upper()
        
        r = requests.get(f"https://api.pwnedpasswords.com/range/{first_five}")
        cracked = re.findall(f"{last_part}:\d+", r.text)
   
        if not cracked:
            return 0
        else:
            cracked = int(cracked[0].split(":")[1])
            return cracked
        

def main():
    parser = argparse.ArgumentParser(description="Strong password generator")
    parser.add_argument("plaintext", type=str, help="String to create password")
    args = parser.parse_args()

    generator = Generator()
    strong_password = generator.generate(args.plaintext)

    print(f"Strong password: {strong_password}")

    cracked = generator.check_password(strong_password)

    if not cracked:
        print("The password has not been pwned!")
    else:
        print(f"The password is Pwned {cracked} times!")
    print()


if __name__ == "__main__":
    main()
