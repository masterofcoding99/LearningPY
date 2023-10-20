import numpy as np

#--------------------------------------------------------------------------------------------------

a = np.array(69) # This is a 0 dimensional arra
b = np.array([1,2,3,4]) # This is a 1 dimensional array
c = np.array([[1,2,3,4], # This is a 2 dimensional array
	     [5,6,7,8]])
d = np.array([[[1,2,3],[4,5,6],[7,8,9]]]) # This is a 3 dimensional array

print(a.ndim)
print(b.ndim) # The 'ndim' command will show how many dimensions there are in the array
print(c.ndim) # Not to be confused with 'ndmin'!
print(d.ndim)

e = np.array([1,2,3,4,5], ndmin=5) # The 'ndmin' command is used to define the number of dimensions
print(e)
print('number of dimensions: ', e.ndim)

#--------------------------------------------------------------------------------------------------



