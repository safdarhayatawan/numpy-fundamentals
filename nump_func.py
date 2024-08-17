import numpy as np
# array functions
a = np.arange(12).reshape(3,4)
a2 = np.arange(12,dtype=float).reshape(4,3)
# print(a,a2)

# max min prod sum
# o means col and 1 means row in axis
# print(np.max(a),np.min(a),np.sum(a),np.prod(a))
# print(a2,np.max(a2,axis=1))#here we find tha max in each row by axis=1
# print(np.mean(a2))
# print(np.median(a2,axis=1))

# trignometric
# print(np.sin(a2))

# dot product where 1sts col and 2nd rows are samw
# print(np.dot(a,a2)) 

# log and exponent
# print(np.log(a))
# print(np.exp(a))

# round floor and ceil
print(np.round(np.random.random((2,3))*100))