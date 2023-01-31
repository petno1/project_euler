def is_pandigital(n, length=None):
    n = str(n)
    if '0' in n:
        return False
    if length and len(n) != length:
        return False
    digits = {int(d) for d in n}
    return len(digits) == len(n) and max(digits) == len(n)



def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

primes = get_primes(20000000 )
primes.sort()
primes.reverse()
largest_pan = 0
for p in primes:
    if is_pandigital(p):
        print(p)
        break