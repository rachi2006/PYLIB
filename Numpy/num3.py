# Array reshaping and transformation in array
"""
* reshape() - reshaping the array or converting 1d to 2d.
* using -1 in reshape - numpt automatically calculate  one dimension.
* flatten() - it convertes multi dimension arrays into one dimension arrays
* ravel() = flatten()
* transpose() - converts R - C, C - R. or u can also use variable_name.T
* resize() - chnage the array shape permanently unlike reshape.
"""
import numpy as np
a = np.array([1,2,3,4,5,6])
b = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])
c = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]],
])

print("reshaping the array: ", a.reshape(2,3))
print("reshaping the array: ", b.reshape(3,4))
print("reshaping the array: ", c.reshape(1,8))

print("using -1 in a reshaping\n: ", a.reshape(2,-1))
print("using -1 in b reshaping\n: ", b.reshape(3,-1))
print("using -1 in c reshaping \n: ", c.reshape(2,-1))

print("converting any array to single array:", b.flatten())
print("converting any array to single array:", c.flatten())

print("using ravel()  to b : ", b.ravel()) # as has flatten()

print("using transpose() in b : \n", b.transpose())
print("using transpose() in c : \n", c.transpose())


print("using resize modifying original array: ", b.reshape((3,4)))