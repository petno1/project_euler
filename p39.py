import numba

@numba.jit
def count_solutions(p):
    count = 0
    for a in range(1, p):
        for b in range(a, p):
            c = p - a - b
            if c > 0:
                if c*c == a*a + b*b:
                    count += 1
    return count

max_solutions = 0
max_p = 0
for p in range(1, 1001):
    solutions = count_solutions(p)
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p

print(max_p)