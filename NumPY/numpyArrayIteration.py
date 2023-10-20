import numpy as np

#-------- Iterating 1D Arrays --------

a = np.array([1,2,3]) # Using a simple for loop we can print out each element of an array
for x in a:
	print(x)

#-------- Iterating 2D Arrays --------

b = np.array([[1,2,3],[4,5,6]]) # If you want all the elements by themselves you would need to have 2 for loops
for y in b:
	for z in y:
		print(z)

#-------- Iterating 3D Arrays --------

c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # Essentially you need as more for loops as there are dimensions in these cases.
						       # This can be annoying if you have especially large arrays
for e in c:
	for f in e:
		for g in f:
			print(g)

#-------- Iterating Arrays with nditer() --------

d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

for h in np.nditer(d): # The nditer() function produces the same result as the for loops did for the previous example
	print(h)
