import numpy as np

array = np.genfromtxt('Numpy_Array.txt', delimiter=',')
# print(array)

# Changing the type of the data
array = array.astype('int32')
print(array)
