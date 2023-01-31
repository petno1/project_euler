import numpy as np
import scipy.special

def str_np(num):
    num = str(num)
    arr = np.ones(len(num))
    for i,s in enumerate(num):
        arr[i] = int(s)
    return int(np.sum(scipy.special.factorial(arr)))

total_sum = 0

for i in range(10,50000):
    if i == str_np(i):
        total_sum += i
        

print(total_sum)