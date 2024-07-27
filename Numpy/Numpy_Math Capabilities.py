import numpy as np

# array = np.array([[1, 2, 3], [4, 5, 6]])

# add 2 to each element, subtraction multiplication and division is done in the same way
# array += 2
# print(array)

# array2 = np.array([[3, 2, 1], [6, 5, 4]])
# print(array2 + array)

# Raising an array to some power
# print(array ** 2)

# we can get values of trigonometric functions of arrays
# print(np.cos(array))

# LINEAR ALGEBRA WITH NUMPY
# a = np.ones((2, 3))
# b = np.full((3, 2), 2)

# print(np.matmul(a, b)) # for this calculation the columns of the first matrix must be equal to the rows of the second matrix

# determining the determininat of a matrix
# matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np.linalg.det(matrix))

# STATISTICS WITH NUMPY
array = np.array([[1, 2, 3], [4, 5, 6]])
# print(np.max(array)) # max of the whole array
# print(np.min(array)) # min of the whole array
# print(np.max(array, axis=1)) # max of each row
# print(np.median(array)) # median of the array
# print(np.sum(array)) # the sum of all the elements in the array
# print(np.sum(array, axis=1)) # sum of each row
# print(np.sum(array, axis=0)) # sum of each column

# REORGANIZING ARRAYS
initial_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# print("Initially the array is in the form: \n", initial_array)
new_array = initial_array.reshape(4, 2)
# print("The New Array Is In The Form: \n", new_array)

# VERTICALLY STACKING VECTORS
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
# print(np.vstack((v1, v2))) # vertically stacking vectors
# OR
# print(np.vstack([v1, v2, v1, v2]))

# HORIZONTALLY STACKING VECTORS
# print(np.hstack((v1, v2))) # horizontally stacking vectors