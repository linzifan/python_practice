# coding: utf-8
text_file = open("romeo.txt")
WORDS = []
for line in text_file:
    words = line.split()
    for word in words:
        if word not in WORDS:
            WORDS.append(word)
WORDS.sort()
print WORDS
text_file = open("romeo.txt")
words = []
for line in text_file:
    word = line.split()
    for w in word:
        words.append(w)
words.sort()
print words
words_dic = {}
for word in words:
    if word not in words_dic:
        words_dic[word] = 0
        for item in words:
            if item == word:
                words_dic[word] += 1
print sorted(words_dic.items())



import csv

text_file = open("anothertext.txt")
words = []
for line in text_file:
    word = line.split(" ")
    for w in word:
        w = w.rstrip("\n")
        w = w.rstrip(",")
        w = w.rstrip(".")
        w = w.rstrip(";")
        w = w.rstrip(":")
        w = w.lstrip("(")
        w = w.rstrip(")")
        
        words.append(w)

words.sort()
print words
words_dic = {}
for word in words:
    if word not in words_dic:
        words_dic[word] = 0
        for item in words:
            if item == word:
                words_dic[word] += 1
print words_dic


writer = csv.writer(open('dict.csv', 'wb'))
for key, value in words_dic.items():
    writer.writerow([key, value])