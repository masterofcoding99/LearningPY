import numpy as np

#-------- Reshape from 1-D to 2-D ---------------

a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newa = a.reshape(4, 3) # This will reshape into a 2D array with 4 arrays each containing 3 elements
print(newa)

#-------- Reshape from 1-D to 3-D ---------------

b = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

newb = b.reshape(2, 3, 2) # This will reshape into 2 arrays that contain 3 arrays, each with 2 elements
print(newb)

# Note that you can't just reshape anything, they need to be compatible
# Also reshapes are a view, so will return the original array

#-------- Unknown Dimension ---------------

c = np.array([1,2,3,4,5,6,7,8])
newc = c.reshape(2,2,-1) # This will reshape into a 3D array with 2x2 elements, the -1 is the unknown dimension. You can only have one
print(newc)

#-------- Flattening the arrays ---------------

d = np.array([[1,2,3],[4,5,6]])
newd = d.reshape(-1) # This will flatten a multidimensional array down to a 1D array
print(newd)
