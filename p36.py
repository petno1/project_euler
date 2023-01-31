def mirror_int(n):
    n = str(n)
    return int(n[::-1])

count = 0
for i in range(1000000):
    base_10_mirror = mirror_int(i)
    base_2 = format(i, 'b')
    base_2_mirror = mirror_int(base_2)
    if int(base_2) == base_2_mirror and i == base_10_mirror:
        count += i
        
print(count)