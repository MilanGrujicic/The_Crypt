from urllib.request import urlopen
import hashlib

def reverse_hash(hash):
    password_list = str(
        urlopen(
            "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
        ).read(),
        "utf-8",
    )
    for password in password_list.split("\n"):
        guess = hashlib.sha3_512(bytes(password, "utf-8")).hexdigest()
        if guess == sha3_512_hash:
            print("[+] The password is: " + str(password))
            break
        elif guess != sha3_512_hash:
            continue
        else:
            print("The password does not matched in the list…")

sha3_512_hash = input("[+] Enter sha3-512 Hash value: ")

reverse_hash(sha3_512_hash)