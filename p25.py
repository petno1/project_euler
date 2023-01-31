F_1 = 1
F_2 = 1
for i in range(10000):
    F_3 = F_2 + F_1
    F_1 = F_2
    F_2 = F_3
    if F_3 >= 10**999:
        print(i+3)
        break