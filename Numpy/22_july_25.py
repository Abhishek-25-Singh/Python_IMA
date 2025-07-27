import numpy as np
?np.ones
np.ones(5)
# Check Total Memory Used
arr = np.ones(5)
print("Total Memory in bytes :",arr.nbytes)
arr = np.ones(5)  # dtype = float64 by default
print("Array:", arr)
print("Item size:", arr.itemsize)   # 8 bytes per float
print("Total elements:", arr.size)  # 5 elements
print("Total Memory (nbytes):", arr.nbytes)  # 5 × 8 = 40 bytes
print(np.ones(5))
print(np.ones(5,dtype=int))
np.ones((5,), dtype=int)
