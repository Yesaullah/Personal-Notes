import numpy as np

# BOOLEAN MASKING AND ADVANCED INDEXING

filedata = np.genfromtxt('Numpy_Array.txt', delimiter=',')

# print(filedata > 50) # returns Booleans for wherever the condition is true or false

# print(filedata[filedata > 50]) # return the values in the array which meet the condition

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# print(array[[2, 3, 8]]) # returns the elements at index 2, 3, and 8

# print(np.any(filedata > 50, axis=0)) # this checks for a value greater than 50 in each column
# print(np.any(filedata > 50, axis=1)) # this checks for a value greater than 50 in each row

# print(np.all(filedata > 50, axis=0)) # this checks if all values are greater than 50 in each column
# print(np.all(filedata > 50, axis=1)) # this checks if all values are greater than 50 in each row