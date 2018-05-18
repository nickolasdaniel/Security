import random
import argparse

def substitute(text):

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    print("Alphabet:    " + "".join(alphabet))

    random_key = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(random_key)
    print("Random key:  " + "".join(random_key))

    print("Plain text:  " + "".join(text))

    cipher = ""
    for i in range(len(text)):
        if text[i] == " " or text[i] == text[i].upper():
            cipher += text[i]
        for j in range(len(random_key)):
            if text[i] == alphabet[j]:
                cipher += random_key[j]

    print("Cipher text: " + "".join(cipher))

input = input("Enter text: ")
substitute(input)
