import numpy as np

# Multi-Dimensional Array

array1 = np.array('A')
array2 = np.array(['A','B','C'])
array3 = np.array([['A','B','C'],
                   ['D','E','F'],
                   ['G','H','I']])
array4 = np.array([
                  [['A','B','C'],['D','E','F'],['G','H','I']],
                  [['J','K','L'],['M','N','O'],['P','Q','R']],
                  [['S','T','U'],['V','W','X'],['Y','Z',' ']]
                  ])

# For checking dimensions of an array , we use 'ndim'
print(array1.ndim)
print(array2.ndim)
print(array3.ndim)
print(array4.ndim)

# For checking the Shape we use 'shape
print(array1.shape)
print(array2.shape)
print(array3.shape)
print(array4.shape)

# Printing word "ALI" using array4
word = array4[0,0,0] + array4[1,0,2] + array4[0,2,2]
print(word)