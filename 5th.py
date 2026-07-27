import numpy as np

# Vectorized Math Funcs

array = np.array([1.32 , 2.67 , 3.99])

print(np.sqrt(array))
print(np.round(array))
print(np.ceil(array))
print(np.floor(array))
print(np.pi)

# taking an array of radii and calculating the area of circle

radii = np.array([4.56 , 8.41 , 3.19])
print(np.pi * radii ** 2)
