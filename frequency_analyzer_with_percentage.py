#!/usr/bin/env python
"""
Author: Mehmet Başaran,
15,03,2020
CENG482 Assignment5_121180015 
"""
from operator import itemgetter
import string
testtext = open('LoveInTheTimeOfCholera.txt', 'r', encoding="utf8").read()
testtext = testtext.lower()
enletfreq = open('EnglishLetterFrequency.txt', 'r', encoding="utf8").read().split()
alphabets = (string.ascii_lowercase, string.ascii_uppercase)
def flatten_array(input):
    tmp_list = []
    for i in input:
        for j in i:
            tmp_list.append(j)
    return tmp_list

def merge_arrays(percents,letnumber):
    m = 0
    for i in range(2,78,3):
        letnumber.insert(i, round(percents[m],2))
        m= m+1
    return letnumber

def cesar_encryption(text, step, alphabets):

    def shift(alphabet):

        return alphabet[step:] + alphabet[:step]

    cesar_alphabets = tuple(map(shift, alphabets))
    alphabets = ''.join(alphabets)
    shifted_alphabets = ''.join(cesar_alphabets)
    converter = testtext.maketrans(alphabets, shifted_alphabets)
    return text.translate(converter)

def count_letter_frequencies(text):
    
    frequencies = {}

    for asciicode in range(65, 91):
        frequencies[chr(asciicode)] = 0

    for letter in text:
        asciicode = ord(letter.upper())
        if asciicode >= 65 and asciicode <= 90:
            frequencies[chr(asciicode)] += 1

    sorted_by_frequency =  sorted(frequencies.items(), key = itemgetter(1), reverse=True)

    return sorted_by_frequency

def percentage_letter_frequencies(text):
    text = flatten_array(text)## flat 2d array to 1d keeping the order
    t = 0
    tmplist =[]
    for i in range(1,52,2):
        t += int(text[i])
    for i in range (1,52,2):
        tmplist.append( int(text[i])  / t * 100 )
    return tmplist
def percentage_letter_frequencies_1d(text):
    #text = flatten_array(text)## flat 2d array to 1d keeping the order
    t = 0
    tmplist =[]
    for i in range(1,52,2):
        t += int(text[i])
    for i in range (1,52,2):
        tmplist.append( int(text[i])  / t * 100 )
    return tmplist

def calculate(text):
    count = count_letter_frequencies(text)
    percent = percentage_letter_frequencies(count)
    count = flatten_array(count)
    m = 0
    for i in range(2,78,3):
        count.insert(i, round(percent[m],2))
        m= m+1
    return count

def calc_eng_alph_freq(enletfreq):
    tmplist = (percentage_letter_frequencies_1d(enletfreq))
    return merge_arrays(tmplist,enletfreq)

print("English Letter Frequencies Statistic")
print(calc_eng_alph_freq(enletfreq))
print("*"*170)
print("Novel Letter Frequencies Analysis")
print(calculate(testtext))
print("*"*170)
print("Cesar encrypted novel Letter Frequencies Analysis")
print(count_letter_frequencies(cesar_encryption(testtext, step=3, alphabets=alphabets)))