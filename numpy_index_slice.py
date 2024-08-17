'''General Slicing Syntax

arr[start:stop:step] for 1D arrays
arr[row_start:row_stop:row_step, col_start:col_stop:col_step] for 2D arrays
arr[x_start:x_stop:x_step, y_start:y_stop:y_step, z_start:z_stop:z_step] for 3D arrays
Key Points:

The start index is inclusive, while the stop index is exclusive.
If start is omitted, it defaults to 0.
If stop is omitted, it defaults to the end of the dimension.
If step is omitted, it defaults to 1.
Negative indices can be used for indexing from the end.
Additional Notes:

NumPy supports higher-dimensional arrays (4D, 5D, etc.), but the slicing concept remains similar.
You can combine slicing with other array operations like indexing, masking, and fancy indexing for more complex manipulations.
Understanding slicing is crucial for efficient data manipulation and analysis in NumPy.
'''
import numpy as np
# array functions
# indexing
a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8,dtype=float).reshape(2,2,2)
# print(a1,a2,a3)
# print(a1[1])
# print(a2[2,3])# here first is row and 2nd is col
# print(a3[0,0,1])# first entry is for which 2d it is and rest is same
# print(a3[1,1,1])# first entry is for which 2d it is and rest is same

# slicing
# print(a1[2:5])
# print(a1[-5:8])
# print(a2[0,:])#0 means 1st row and : means every col
# print(a2[:,2])#: means every row and 2 means 2nd col
# print(a2[1:,1:3])#
# print(a2[::2,::3])#
# print(a2[::2,1::2])#

# log and exponent of array
# print(np.log(a2))
# print(np.exp(a2))

# slicing of 3d array
a3 = np.arange(27).reshape(3,3,3)
# print(a3[0,1])
# print(a3[1,:,1])
# print(a3[2,1:,1:])
# print(a3[::2,0,::2])

# iteration over arrays
# for i in a1:
#  print(i)
# for i in a2:
#  print(i)
# for i in a3:
#  print(i)
# for i in np.nditer(a3):
#     print(i)

# transpose  row to col and col to rows
# print(np.transpose(a2))
# or another way is
# print(a2.T)

# ravel a method to convert any array into 1d
# print(a2.ravel())

# stacking means splicing
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
# print(np.hstack((a4,a5)))#horizantal
# print(np.vstack((a4,a5)))#horizantal


# splitting arrays
# print(np.hsplit(a4,2))

# numpy array vs list time comparison
a= [i for i in range (1000000)]
b = [i for i in range(1000000,2000000)]
c = []
import time
# start = time.time()
# for i in range(len(a)):
    # c.append(a[i] + b[i])
# print(time.time()- start)
a = np.arange(1000000)
b = np.arange(1000000,2000000)
c= a+b
start = time.time()
print(time.time()- start)