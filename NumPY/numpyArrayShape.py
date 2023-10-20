import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape) # This will print out (2, 4) which means 2 dimensions each with 4 elements

b = np.array([1,2,3,4], ndmin=5)
print(b)
print('shape of array: ', b.shape) # As the array was forced to 5 dims the shape will read (1,1,1,1,4)
