import numpy as np

total_array = np.zeros((900,900))
for i in range(900):
    total_array[i,:] += np.arange(100,1000)

total_array = total_array*total_array.T

def palindrome_integer(number): 

    if not isinstance(number, int):
        return 0
    elif str(number) == str(number)[::-1]:
        return number
    else:
        return 0
    
largest_pal = 0
for i in range(900):
    for j in range(900):
        palindrome = palindrome_integer(int(total_array[i,j]))
        if palindrome > largest_pal:
            largest_pal = palindrome
print(largest_pal)