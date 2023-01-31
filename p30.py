import numpy as np

def five_pow(n):
    n = str(n)
    arr = np.zeros(len(n))
    for i,s in enumerate(n):
        arr[i] = int(s)
    return np.sum(arr**5)

pow_sum = 0
for j in range(1000,200000):
    if j == five_pow(j):
        pow_sum += j
    
print(pow_sum)