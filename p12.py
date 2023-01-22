def divisors(n):
    divisors = 0
    for i in range(1, int(n**(0.5))+1):
        if n % i == 0:
            divisors += 2
    return divisors

def triangle_number(n):
    return sum(range(1, n+1))

triangle_num = 1
counter = 1
while divisors(triangle_num) <= 500:
    counter += 1
    triangle_num = triangle_number(counter)

print(triangle_num)