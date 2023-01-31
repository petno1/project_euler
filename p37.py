def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def left_trunc(N):
    N = str(N)
    for i in range(len(N)):
        yield int(N[i:])
        
def is_left(n, primes):
    return set(left_trunc(n)).issubset(primes)

def right_trunc(N):
    N = str(N)
    l = len(N)
    for i in range(len(N)):
        yield int(N[:l - i])
        
def is_right(n, primes):
    return set(right_trunc(n)).issubset(primes)


count = 0
count_sum = -17
primes = set(get_primes(1000000))
for p in primes:
    if p == 3797:
    if is_right(p, primes) and is_left(p, primes):
        count_sum += p
        count += 1
        
print(count_sum)