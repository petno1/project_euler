import numpy as np
with open(r"C:\Users\Peter\Documents\nyback\Documents\Euler\p42_words.txt", 'r') as file:
        names = file.readlines()
        names = names[0]
        names = names.replace('"', '')
        names = names.split(',')

def alphabetical_value(string):
    alphabetical_value = 0
    for character in string.lower():
        alphabetical_value += ord(character) - ord('a') + 1
    return alphabetical_value

def t_n(n):
    return n*(n+1)//2

n = np.arange(50)
t = t_n(n)

count = 0
for s in names:
    if alphabetical_value(s) in t:
        count += 1

print(count)

