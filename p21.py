def sum_divisors(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)

result = 0
seen = set()
for i in range(1, 10000):
    divisors_sum = sum_divisors(i)
    if i != divisors_sum and sum_divisors(divisors_sum) == i:
        if i not in seen:
            result += i
            seen.add(i)
        if divisors_sum not in seen:
            result += divisors_sum
            seen.add(divisors_sum)
print(result)
