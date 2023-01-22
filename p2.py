def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1) 

fib_nr = 0
total = 0
count = 0
while fib_nr <= 4*10**6:
    fib_nr = fib(count)
    if fib_nr % 2 == 0:
        total += fib_nr
    count += 1
    
print(total)