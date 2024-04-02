from urllib.request import urlopen
import hashlib

def reverse_hash(hash, wordlist):
    '''Compares the provided hash with the hashed passwords from wordlist.'''
    for password in wordlist.split("\n"):
        guess = hashlib.sha3_512(bytes(password, "utf-8")).hexdigest()
        if guess == hash:
            print("[+] The password is: " + str(password))
            break
        elif guess != hash:
            continue
        else:
            print("The password does not matched in the list…")

ten_million_password_list = str(
    urlopen(
        "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
    ).read(),
    "utf-8",
)

sha3_512_hash = input("[+] Enter sha3-512 hash value: ")

reverse_hash(sha3_512_hash, ten_million_password_list)
