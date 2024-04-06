from urllib.request import urlopen
import hashlib
import sys
import time
import logo

def load_spinner():
    '''Displays a spinner animation using basic ASCII characters.'''
    for char in '|/-\\':
        sys.stdout.write('\r' + char)
        sys.stdout.flush()
        time.sleep(0.1)

def load_wordlist():
    '''Loads a 10 million password list.'''
    print("[-] Loading wordlist... Please wait.")
    ten_million_password_list = str(
        urlopen(
            "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
        ).read(),
        "utf-8",
    )
    return ten_million_password_list

def reverse_hash(hash):
    '''Compares the provided hash with the hashed passwords from wordlist.'''
    wordlist = load_wordlist()
    password_not_found = True
    print("\n[-] Checking passwords... Please wait.")
    while password_not_found:
        load_spinner()
        for password in wordlist.split("\n"):
            guess = hashlib.sha3_512(bytes(password, "utf-8")).hexdigest()
            if guess == hash:
                print("\n[+] The password is: " + str(password))
                password_not_found = False
                break
            elif guess != hash:
                continue
            else:
                print("\nThe password does not matched in the list…")

print(logo.logo)

sha3_512_hash = input("[+] Enter sha3-512 hash value: ")

reverse_hash(sha3_512_hash)
