import numpy as np

three = np.arange(3, 1000, 3)
five = np.arange(5, 1000, 5)
total = np.concatenate([three, five])
total = np.unique(total)
print(np.sum(total))