# coding: utf-8
import string
content = raw_input("> ")
filtered = open('filtered_words.txt','r')
filtered_list = []
for line in filtered:
    filtered_list.append(line.strip('\n'))
for word in filtered_list:
    content = string.replace(content, word, "*"*len(word.decode('utf-8')))
print content
