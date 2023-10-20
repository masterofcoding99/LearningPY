import numpy as np

#-------- Joining 1D Arrays ----------

a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.concatenate((a, b)) # This will create a new array with the contents of both
print(c)

#-------- Joining 2D Arrays ----------

d = np.array([[1,2],[3,4]])
e = np.array([[5,6],[7,8]])

f = np.concatenate((d, e), axis=0)
print(f)

#-------- Joining Arrays Using stack() Function ----------

g = np.array([1,2,3])
h = np.array([4,5,6])

i = np.stack((g, h), axis=1) # Depending on the axis argument given this will display different things
print(i)

#-------- Stacking along rows hstack() ----------

j = np.array([1,2,3])
k = np.array([4,5,6])

l = np.hstack((j, k)) # This result will look very similar to the joining 1D arrays
print(l)

#-------- Stacking along columns vstack() ----------


m = np.array([1,2,3])
n = np.array([4,5,6])



