from math import sqrt

def find_abundant(limit):
    abundant_numbers = []
    for i in range(1, limit+1):
        factors = [x for x in range(1, int(sqrt(i))+1) if i%x == 0]
        factors = sum(factors + [i//x for x in factors if x*x!=i]) - i
        if factors > i:
            abundant_numbers.append(i)
    return abundant_numbers

def sum_of_positive_integers(limit):
    abundant_nums = find_abundant(limit)
    bitset = [False]*(limit+1)
    for i in range(len(abundant_nums)):
        for j in range(i, len(abundant_nums)):
            abundant_sum = abundant_nums[i] + abundant_nums[j]
            if abundant_sum <= limit:
                bitset[abundant_sum] = True
    return sum(i for i, is_abundant in enumerate(bitset) if not is_abundant)

print(sum_of_positive_integers(28123))