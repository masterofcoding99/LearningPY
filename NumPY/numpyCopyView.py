import numpy as np

#--------- COPY ----------

a = np.array([1,2,3,4,5])
x = a.copy() # The copy that is made should'nt be affected by the original changes
a[0] = 42
print(a)
print(x)

#--------- VIEW ----------

b = np.array([1,2,3,4,5])
y = b.view() # Both versions should be affected by the changes in this instance
b[0] = 42
print(b)
print(y)

#--------- Check if Array owns data ----------

c = np.array([1,2,3,4,5])
l = c.copy()
m = c.view()

print(l.base) # This will return 'None'
print(m.base) # This will return the original array
