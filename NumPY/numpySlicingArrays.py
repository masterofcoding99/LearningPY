import numpy as np

a = np.array([1,2,3,4,5,6,7])
print(a[1:5]) # This will slice out the elements from the index 1 through 5
print(a[4:]) # This will print the elements from 4th to the end
print(a[:4]) # This will print all the elements up till the 4th

#------------- Negative Slicing --------------------------------------------

print(a[-3:-1]) # This will print 3 from the end to 1 from the end

#------------- Using Step --------------------------------------------------

print(a[1:5:2]) # This will print every other element from index 1 through 5
print(a[::2]) # This will print every other element in the array

#------------- Slicing 2-D Arrays -------------------------------------------

b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)
print(b[1, 1:4]) # This will print the elements from the second element (index 1 through 4(not included))
print(b[0:2, 2]) # This will print the second element from both arrays
print(b[0:2, 1:4]) # This will print a 2-D array of the requested elements
