import numpy as np
#  creating 1d 2d and 3d arrays 
a = np.array([1,2,3])#one d array or vector
b= np.array([[1,2,3],[4,5,6]])#2d array or metrics
c=np.array([[[[1,2],[3,4],[5,6],[7,8]]]])#3d arry or Tensor
# creating float and bool type arays
d = np.array([1,2,3],dtype=float)
e = np.array([1,2,3],dtype=bool)

# np.arange and reshape

aa = np.arange(1,11)
# print(aa)

aa = np.arange(1,11,2).reshape(5,1)
# print(aa)

bb = np.arange(1,11).reshape(5,2)#5r and 2 col
cc = np.arange(1,11).reshape(2,5)#2r and 5 col
dd = np.arange(1,13).reshape(3,4)
# print(bb,cc,dd)
# u can give any shape within range
# reshape with rows and columns specific

# np.ones and zerpes
q = np.ones((3,4))
qq = np.zeros((3,2))
# print(q,qq)

# np.random
w = np.random.random((3,4))
# print(w)

# np.linspace 3params least upper and total desired values
e = np.linspace(-9,9,9)
print(e)
