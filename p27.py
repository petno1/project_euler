from operator import eq
import numpy as np
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def prime_quad(a,b, n):
    return n**2 + a*n + b

res_max = 0
N = 500
primes = set(get_primes(N))
for a in range(-1000, 0):
    for b in range(0, 1001):
        res = len(primes.intersection(list(prime_quad(a,b,np.arange(N)))))
        if res > res_max:
            res_max = res
            A = a
            B = b
print(A*B)
        
        
    