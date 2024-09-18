import logo
import utils

print(logo.logo)

print("Type 'c' to exit.\n")

sha3_512_hash = input("[+] Enter sha3-512 hash value: ")

if sha3_512_hash in 'Cc':
    import sys
    sys.exit()

utils.reverse_hash(sha3_512_hash)
