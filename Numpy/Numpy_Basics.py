import numpy as np

# simple aray
a = np.array([1, 2, 3])
print(a)

# 2D Array
b = np.array([[2.0, 3.0, 4.0], [6.0, 7.0, 8.0]])
print(b)

# How to get dimensions of an array
print(b.ndim) # dimensions of array b

# How to get shape of an array
print(b.shape) # array b is a 2x3 array

# How to get the datatype of an array
print(a.dtype) 
print(b.dtype)

# We can set the datatype/size of an array by ourselves
sized_array = np.array([1, 2, 3], dtype='int16')
print(sized_array.dtype)

# How to get the size of an element of an array
print(a.itemsize)
print(b.itemsize)
print(sized_array.itemsize)

# How to get the size of the whole array
print(a.nbytes)
print(b.nbytes)
print(sized_array.nbytes)