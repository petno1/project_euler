def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(600855)
prime_factors = []
for p in primes:
    if 600851475143 % p == 0:
        prime_factors.append(p)
        
print(prime_factors[-1])