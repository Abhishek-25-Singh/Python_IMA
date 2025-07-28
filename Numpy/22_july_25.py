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


S_3D = (3,2,4)    #shape(3,3,2) 3Dimension Array
print(np.ones(S_3D))
print(np.ones(S_3D,dtype=int))

#3D Array with all ones in Floating Values
# Shape =(2,2,2) 2 Block, 2 Row, 2 Column
S = (2,2,2)
Array_3D = np.ones(S)
print(Array_3D)


# 3D Array with all ones in Integer 
# Shape = (2,2,2) 2blocks,each with 2 rows and 2 columns
s = (2,2,2)
Array_3D = np.ones(s,dtype = int)
print(Array_3D)
# Output: Two 2×2 matrices (2 rows × 2 columns), filled with 1

_1D=np.ones((2))
S_2D=np.ones((2,2))   # 2 rows , 2 columns
S_3D=np.ones((3,2,3)) # 3 blocks, 2 rows and 3 columns
S_3D=np.ones((3,3,2)) # 3 blocks, 2 rows and 3 columns
print(S_3D)


np.ones((2,1),dtype=int)
np.ones((2,2),dtype=int)
np.ones((3,3),dtype=int)

S_1D=np.ones((2),dtype=int)
S_2D=np.ones((2,2),dtype=int)   # 2 rows , 2 columns
S_3D=np.ones((3,2,3),dtype=int)
S_3D=np.ones((3,3,2),dtype=int)# 3 blocks, 2 rows and 3 columns
print(S_3D)
