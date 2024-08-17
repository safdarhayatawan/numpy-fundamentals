import numpy as np
# ndim provides dimension of an array
a = np.arange(10)
aa = np.arange(12,dtype=float).reshape(3,4)
aaa = np.arange(8).reshape(2,2,2)
# print(aa.ndim)
# print(aa)
# print(a.dtype,aa.dtype,aaa.dtype)

# shape
# print(aa.shape)# here 2 arrays of having shape 2,2 which means 2 rows and 2 col
#size
# print(aa.size)# provide total items of an array

# item size

# print(a.itemsize)#provide bytes of items

aq = np.arange(10,dtype=np.int64)
# print(aq.itemsize)

 # changing data type of array

a3 = np.arange(8)
# print(a3.astype(np.int32))
# print(a3.dtype)

# Array mathematical operations
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)
# print(a1,a2)
#scaler operations meaning 1 multply or
# print(a1 * 2,a2 + 2,a1 / 2)

#relational operator on arrays
# print(a1 > 5,a2 == 15)

# vector operations arithmatic
print(a1,a2,a1 + a2)
# 1st element will be added with the same element of other array
