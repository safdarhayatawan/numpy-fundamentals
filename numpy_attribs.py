import numpy as np
# ndim provides dimension of an array
a = np.arange(10)
aa = np.arange(12,dtype=float).reshape(3,4)
aaa = np.arange(8).reshape(2,2,2)
# print(aa.ndim)
# print(aa)
# print(aa.shape)# here 2 arrays of having shape 2,2 which means 2 rows and 2 col
print(aa.size)


 