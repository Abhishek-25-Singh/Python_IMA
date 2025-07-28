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
#🔤 1. With Strings
msg = "hello"
print("Value for humans :    ",msg)
print("Value for the python:",repr(msg))

#🔢 2. With Numbers
num = 42
print(num)       # Output: 42 ➡️ Same output here — because number doesn't need special formatting.
print(repr(num)) # Output: 42 ➡️ Same output here — because number doesn't need special formatting.

# 🧮 3. With a NumPy Array
arr = np.ones(3)
print("arr Using Print function :",arr)
print("Using Representation Function :",repr(arr)) #➡️ repr() tells you it's a NumPy array, not just a list of numbers.

np.ones(5)


# Check Total Memory Used
arr = np.ones(5)
print("Total Memory in bytes :",arr.nbytes)

arr = np.ones(5)
print("Array : ",arr)
print("Item Size :",arr.itemsize)
print("Total Element :",arr.size)
print("Total Memory in byte :",arr.nbytes)

np.ones(5,dtype=int)


print(np.ones(5))
print(np.ones(5,dtype=int))


np.ones((5,))


np.ones((5,), dtype=int)

print(np.ones(5,))
print(np.ones((5,),dtype=int))

s = np.ones((5),dtype = int)
print(s)
print("Type of s : ",type(s))


 IN 2D Array
np.ones((2,1)) #(2 Rows X 1 columns)

np.ones((2,2)) #(2 Rows X 2 columns)
np.ones((3,3)) #(3 Rows X 3 columns)


s = (2,2)
arr=np.ones(s,dtype = int)
print("Array :",arr)
print("Total Memory in bytes :",arr.nbytes)

S_1D = (2)          #shape(2) 1Dimension Array
print(np.ones(S_1D))
print(np.ones(S_1D,dtype=int))

S_2D = (2,2)       #shape(2,2) 2Dimension Array
print(np.ones(S_2D))
print(np.ones(S_2D,dtype=int))
