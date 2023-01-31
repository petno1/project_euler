
def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


def rotation(N):
    N = str(N)
    for i in range(len(N)):
        yield int(N[i:] + N[:i])

def is_circular(n, primes):
    return set(rotation(n)).issubset(primes)

circ_count = 0
primes = set(get_primes(1000000))
for p in primes:
    if is_circular(p, primes):
        circ_count += 1


print(circ_count)
    
        