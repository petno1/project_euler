from itertools import permutations
nums = "0123456789"
num_permutations = list(permutations(nums))
mil_permu = num_permutations[10**6+1]
answer = ""
for s in mil_permu:
    answer += s
    
print(answer)