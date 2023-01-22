#Slow but simple implementation
import numpy as np
all_num = np.arange(20, 10**9, 20)
common = np.copy(all_num)
for i in range(19, 1, -1):
    print(i)
    nums = np.arange(i, 10**9, i)
    common = np.intersect1d(common, nums)
    
print(common[0])