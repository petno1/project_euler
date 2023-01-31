from itertools import permutations

def get_pandigital_numbers():
    pandigital_nums = []
    digits = "0123456789"
    for perm in permutations(digits):
        if perm[0] != "0":
            pandigital_nums.append("".join(list(perm)))
    return pandigital_nums

pan_numbers = get_pandigital_numbers()
primes = [2,3,5,7,11,13,17]

pan_sum = 0
for p in pan_numbers:
    if int(p[7:10]) % 17 == 0 and int(p[6:9]) % 13 == 0 and \
        int(p[5:8]) % 11 == 0 and int(p[4:7]) % 7 == 0 and \
        int(p[3:6]) % 5 == 0 and int(p[2:5]) % 3 == 0 and  \
        int(p[1:4]) % 2 == 0:
        pan_sum += int(p)
        
print(pan_sum)