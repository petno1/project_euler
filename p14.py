longest_chain = 0
longest_num = 0

def collatz(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1
    return count

for i in range(1, 1000000):
    chain_length = collatz(i)
    if chain_length > longest_chain:
        longest_chain = chain_length
        longest_num = i

print(longest_num)