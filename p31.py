import numba

@numba.jit
def faster_loops():
    count = 1 #for the 2 pound bill
    for i in range(0,201):
        for j in range(0, 201, 2):
            for k in range(0, 201, 5):
                for l in range(0, 201, 10):
                    for m in range(0, 201, 20):
                        for n in range(0,201,50):
                            for o in range(0,201, 100):
                                coin_sum = i + j+k+l+m+n+o
                                if coin_sum == 200:
                                    count += 1
    return count
print(faster_loops())

