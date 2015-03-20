
# coding: utf-8

# In[1]:

import random


# In[32]:

def codeGen(number, length = 8):
    codefile = open('codes.txt', 'w')
    if number <= 0:
        return 'invalid number of codes'
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    count = 1
    while True:
        string = ''
        for i in range(length):
            index = random.randint(0, len(char) - 1)
            string = string + char[index]
        codefile.write(string+'\n')
        count += 1
        if count > number:
            break


# In[35]:

codeGen(200)


# In[ ]:



