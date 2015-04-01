# coding: utf-8
import random

CIPHER = {}
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# generate dictionary
def init():
    letter_list = list(LETTERS)
    random.shuffle(letter_list)
    for ch in LETTERS:
        CIPHER[ch] = letter_list.pop()
# encode function
def encode(word):
    code = ""
    for ch in word:
        code += CIPHER[ch]
    return code
# decode function
def decode(code):
    word = ""
    for ch in code:
        for key, value in CIPHER.items():
            if ch == value:
                word += key
    return word
# change dictionary if necessary
init()
# CIPHER

# encode process
word = raw_input("What word you want encode?")
code = encode(word)
print code

# decode process
code = raw_input("What code do you get?")
word = decode(code)
print code + " decodes to " + word
