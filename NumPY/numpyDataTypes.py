import numpy as np

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of mem for other type (VOID)

#---------- Check data type of an Array -----------------

a = np.array([1,2,3,4])
print(a)
print(a.dtype) # This will print out the type of the data that is inside the array - int64 for this example

b = np.array(['Banana','Orange','Apple'])
print(b)
print(b.dtype) # This will again print the type of data -  <U6 for this example

#---------- Creating Arrays with Defined Data Types ------

c = np.array([1,2,3,4], dtype='S') # The 'dtype=' function forces the type of data
print(c)
print(c.dtype) # this will print out that is an S1

d = np.array([1,2,3,4], dtype='i4') # This forces the data to become a 4 byte integer
print(d)
print(d.dtype) # This will print out int32 for this example


#---------- Converting Data Types on Existing Arrays ------

e = np.array([1.1, 2.1, 3.1])

newe = e.astype('i') # This will convert all the data types to an integer, you can also pass (int) here
print(newe)
print(newe.dtype) # This will print 'int32' even though they started off as floats

newer = newe.astype(bool) # This shows you can convert again from the next array and just keep going
print(newer)
print(newer.dtype) # This will print out 'bool' as they have all now been converted to a boolean value

newery = newer.astype('f') # When you try and jump all the way back though this does not work
print(newery)
print(newery.dtype)





