import numpy as np

# Filtering = refers to the process of selecting elements 
#             from an array that matches given condition.

array = np.array([[12, 67, 87, 44, 52, 11, 98, 76],
                  [65, 34, 55, 99, 27, 49, 53, 88]])

teenagers = array[array < 18]
adults = array[array >= 18]
even = array[array % 2 == 0]
odd = array[array % 2 != 0]

print(teenagers)

# but the issue with this is that it will give us the answer in a form of flat array 
# if we want our answer in the original format of the array 
# we use where() function

# syntax = np.where(condition, array, substitute)

seniors = np.where(array >=  65, array, 0)
print(seniors)
