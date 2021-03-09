# Implementation of Caeser(Shift) Cipher

alpha = "abcdefghijklmnopqrstuvwxyz"  # length=26


def encrypt(p, shift=3):
    e = ""
    for c in p.lower():
        index = alpha.index(c)
        newIndex = (index + shift) % len(alpha)
        e += alpha[newIndex]
    return e


def decrypt(e, shift=3):
    p = ""
    for c in e.lower():
        index = alpha.index(c)
        newIndex = (index - shift) % len(alpha)
        p += alpha[newIndex]
    return p

pt = input("Enter text to encrypt : ").lower()
print("Encryption of '{}' is '{}'".format(pt, encrypt(pt)))

ct = input("\nEnter text to decrypt : ").lower()
print("Decryption of '{}' is '{}'".format(ct, decrypt(ct)))
