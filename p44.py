import numpy as np
import numba
def pentagonal_numbers(n):
    return n*(3*n - 1)//2

n = np.arange(1,10000)
p_n = pentagonal_numbers(n)
p_n_set = set(pentagonal_numbers(n))
def find_min():
    min_dif = 1000000000000000000
        
    for i in range(len(p_n)-1):
        for j in range(i+1, len(p_n)):
            if (p_n[j]-p_n[i]) in p_n_set and (p_n[i]+p_n[j]) in p_n_set and abs(p_n[i]-p_n[j]) < min_dif:
                min_dif = abs(p_n[i]-p_n[j])
    return min_dif


print(find_min())
