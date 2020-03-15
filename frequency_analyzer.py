#!/usr/bin/env python
"""
Author: Mehmet Başaran,
15,03,2020
CENG482 Assignment5_121180015 
"""
from operator import itemgetter
import string
str = open('LoveInTheTimeOfCholera.txt', 'r', encoding="utf8").read()
str = str.lower()
alphabets = (string.ascii_lowercase, string.ascii_uppercase)
def count_letter_frequencies(text):

    frequencies = {}

    for asciicode in range(65, 91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[chr(asciicode)] += 1

    sorted_by_frequency = sorted(frequencies.items(), key = itemgetter(1), reverse=True)

    return sorted_by_frequency

def cesar_encryption(text, step, alphabets):

    def shift(alphabet):

        return alphabet[step:] + alphabet[:step]

    cesar_alphabets = tuple(map(shift, alphabets))
    alphabets = ''.join(alphabets)
    shifted_alphabets = ''.join(cesar_alphabets)
    converter = str.maketrans(alphabets, shifted_alphabets)
    return text.translate(converter)

print(count_letter_frequencies(str))
print(count_letter_frequencies(cesar_encryption(str, step=3, alphabets=alphabets)))