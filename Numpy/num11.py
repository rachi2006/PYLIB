# linear algebra in numpy

import numpy as np
a = np.array([
    [1,2],
    [3,4]
])
b = np.array([
    [5,6],
    [7,8]
])
print("\n matrix multiplication :\n ", np.dot(a,b)) # or you can use "@"
print("\n transpose of matrix :", a.T) 
print("\n determinate of matrix :", np.linalg.det(a))
print("\n inverse of matrix a :", np.linalg.inv(a))
print("\n identity of matrix a :", np.eye(3))

#eigen values and vectores:
print("\n")
values, vectors = np.linalg.eig(a)
print("\n eigen value of a: ", values)
print("\n eigen vectors of a : ", vectors)

# we can also slove liner equation:
# 2x+y=5
# x-y=1
print("\n sloving a liner equestion of 2x+y=5, x-y=1 :")
c = np.array([
    [2,1],
    [1,-1]
])

d =np.array([5,1])
print(np.linalg.solve(c,d))