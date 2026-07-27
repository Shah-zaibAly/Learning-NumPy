import numpy as np

# Aggregate Functions

array = np.array([[1,2,3,4],
                  [5,6,7,8]])

print(np.sum(array))
# row-wise 
print(np.sum(array, axis=1))
# column-wise
print(np.sum(array, axis=0))

print(np.prod(array))
print(np.min(array))
print(np.argmin(array)) # gives the position of min
print(np.max(array))
print(np.argmax(array))
print(np.std(array))    # standard deviation
print(np.var(array))    # sqaure of std
print(np.mean(array))