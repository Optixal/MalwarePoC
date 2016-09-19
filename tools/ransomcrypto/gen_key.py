#!/usr/bin/python3

# Optixal

# Generates a random 256-bit key in writes bytes to file

import sys, codecs
from Crypto import Random

def checkreq():
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "[output]")
        sys.exit(1)

def hexify(s):
    return codecs.encode(s, 'hex').decode("UTF-8").upper()

def main():
    checkreq()
    
    key = Random.new().read(32)
    with open(sys.argv[1], 'w') as f:
        f.write(hexify(key) + '\n')

if __name__ == "__main__":
    main()
