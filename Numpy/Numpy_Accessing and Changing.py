import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]) # a 2x7 array

# How to get a specific element, indexing: [row, column]
#print(a[1, 5])

# How to get a complete row
#print(a[0, :]) 

# How to get a complete column
#print(a[:, 2])

# Another approach to extract elements from the array, [start_index : end_index : step_size]
#print(a[0, 0 : 7 : 1]) # this prints the first row starting with index 0, step_size 1, end_index 7

# How to change a specific element
# a[1, 5] = 100 # 100 replaces 13
# print(a)

# How to change the values of a specific row with a same value
# a[1, :] = 50
# print(a)

# How to change the values of a specific column with a same value
# a[:, 3] = 35
# print(a)

# How to change values of a specific row with different values
# a[0, :] = [7, 6, 5, 4, 3, 2, 1]
# print(a)

# How to change values of a specific column with different values
# a[:, 5] = [69, 70]
# print(a)

# 3D array example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(b)
# if we need to access '4' in this array:
#print(b[0, 1, 1])
# if we need to change some value in the 3D array
# b[1, 1, 1] = 69 # here 8 will change to 69
# b[0, :, :] = [[3, 3], [3, 3]]
# print(b)
