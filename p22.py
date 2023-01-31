with open(r"C:\Users\Peter\Documents\nyback\Documents\Euler\p22_names.txt", 'r') as file:
        names = file.readlines()
        names = names[0]
        names = names.replace('"', '')
        names = names.split(',')
names.sort()

def alphabetical_value(string):
    alphabetical_value = 0
    for character in string.lower():
        alphabetical_value += ord(character) - ord('a') + 1
    return alphabetical_value

name_sum = 0

for i,n in enumerate(names):
    name_sum += (i+1)*alphabetical_value(n)

print(name_sum)