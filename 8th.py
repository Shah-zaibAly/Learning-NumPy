import numpy as np 

# Broadcasting in NumPy is the rule system that lets arrays 
# with different shapes work together in arithmetic operations without writing loops.

# NumPy compares shapes from right to left. Two dimensions are compatible if:
# they are the same size or 
# one of them is 1

#EXAMPLES

# 1) Scalar with an array
a = np.array([1, 2, 3])       # size of a = [1,3] and 10 is scalar
print(a + 10)

# 2) 1D array with 2D array
b = np.array([[1, 2, 3],      # size of b = [2,3] and of c = [1,3]
              [4, 5, 6]])

c = np.array([10, 20, 30])

print(b + c)

# 3) Column vector with matrix
d = np.array([[1],           # size of d = [3,1] and of e = [1,3]
              [2],
              [3]])

e = np.array([[10, 20, 30]])

print(d + e)

# 4) Multiplying with broadcasting
f = np.array([[1, 2],        # size of f = [2,2] and of g = [1,2]
              [3, 4]])

g = np.array([10, 100])

print(f * g)

# 5) Adding a 1-column array to a 2D array
h = np.array([[1, 2, 3],     # size of h = [2,3] and of i = [2,1]
              [4, 5, 6]])

i = np.array([[100],
              [200]])

print(h + i)