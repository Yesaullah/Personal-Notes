import numpy as np

# # All 0s matrix
# zero_matrix = np.zeros((2, 3, 2, 3), dtype='int32')
# print(zero_matrix)

# Array of random decimal numbers
# random_matrix = np.random.rand(2, 3)
# print(random_matrix)

# Array of random int numbers
# random_int_matrix = np.random.randint(7, size=(2, 3))
# print(random_int_matrix)

# initializing an identity matrix
# identity_matrix = np.identity(4)
# print(identity_matrix)

# If we want to initialize an array by repeating another array
# repeat_array = np.repeat([[[1, 2, 3]]], 3, axis=1)
# print(repeat_array)

# question:
# array to be made:
#   [[1, 1, 1, 1, 1]
#    [1, 0, 0, 0, 1]
#    [1, 0, 9, 0, 1]
#    [1, 0, 0, 0, 1]
#    [1, 1, 1, 1, 1]]
# array = np.ones((5, 5))
# temp_array = np.zeros((3, 3))
# temp_array[1, 1] = 9
# array[1:4, 1:4] = temp_array
# print(array)

