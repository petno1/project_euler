import numpy as np

sum_square = np.sum(np.arange(1,100+1)**2)
square_sum = np.sum(np.arange(1,100+1))**2

print(square_sum - sum_square)