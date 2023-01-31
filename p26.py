def longest_recurring_cycle(n):
    longest_cycle = 0
    value = 0
    for i in range(2, n):
        if i % 2 != 0 and i % 5 != 0:
            cycle = 1
            while (10 ** cycle) % i != 1:
                cycle += 1
            if cycle > longest_cycle:
                longest_cycle = cycle
                value = i
    return value

print(longest_recurring_cycle(1000))
