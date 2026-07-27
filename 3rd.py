import numpy as np

# Slicing 

array = np.array([
                 [1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]
                 ])

# in slicing [0 , 0] - the first 0 represents the rows and the second 0 represents the column
# we use slicing on the syntax [start:end:step]
# starting index is inclusive whereas ending index in exclusive

print(array[1])      # 2nd row
print(array[-2])     # 2nd last row
print(array[1:3])    # middle two rows
print(array[::2])    # every second row or even rows
print(array[1::2])   # odd rows
print(array[::-1])   # reverse array
print(array[::-2])   # reverse with gap of 2

# by this array[:, 0] , we can select all rows

print(array[:, 0])   # 1st column i.e [1,5,9,13]
print(array[:, 3])   # last column i.e [4,8,12,16]
print(array[:, -2])  # 2nd last column
print(array[:, 0:4]) # all the columns
print(array[:, ::2]) # print columns with gap of 2 or even columns
print(array[:, 1::2])# print odd columns
print(array[:2 , :2])# it gives first 2 columns of the first two rows
print(array[2: , 2:])# last 2 rows of the last 2 columns
print(array[:3 , 2:])# last 2 columns of the fisrt three rows
