import numpy as np

#------------- Accessing 1-D Arrays ------------------------------
a = np.array([1,2,3,4])
print(a)
print(a[0]) # This will print the 1st  item in the array
print(a[1]) # This will print the 2nd item in the array
print(a[2] + a[3]) # This will add 2 items in the array together

#------------- Accessing 2-D Arrays ------------------------------

b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)
print('2nd element on 1st row: ', b[0, 1])
print('5th element on 2nd row: ', b[1, 4])
print('Lat element from 2nd dim: ', b[1, -1])

#------------- Accessing 3-D Arrays ------------------------------

c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(c)
print('3rd element of 2nd array of the 1st array',c[0, 1, 2])
