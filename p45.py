def pentagonal_numbers(n):
    return n*(3*n - 1)//2

def triangle_numbers(n):
    return n*(n+1)//2

def hexagonal_numbers(n):
    return n*(2*n-1)

n = 100000
p_n_set = set(pentagonal_numbers(i) for i in range(165, n+1))
t_n_set = set(triangle_numbers(i) for i in range(285, n+1))
h_n_set = set(hexagonal_numbers(i) for i in range(143, n+1))

common_numbers = t_n_set.intersection(p_n_set, h_n_set)

print(list(common_numbers)[1])
