"""# here we are creating array 
import numpy as  np
arr1 = np.array([1,2,3,4,5,6]) # tis is 1d array
print(arr1)
arr2 = np .array([[1,2],[3,4]]) # this is 2d array
print(arr2)
arr3 = np.array([
[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]
])
print(arr3)
-------------------------------------------------------------------

there is some special arrays
np.zeros((2,3))
np.ones((2,3))
np.arange(0,10,2)
np.linspace(0,1,5)



arr1 = np.zeros((2,3))
print(arr1)
arr2 = np .arange(0,10,2 ) 
print(arr2)
--------------------------------------------------------------
a = [1,2,3]
b = [4,5,6]
result = []
for i in range(len(a)):  #this process is very solw 
    result.append(a[i]+b[i])
print(result)

import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])        # in this no loop needed, faster execution
print(arr1+arr2)
"""

#basics of numpy
import numpy as np 
print("1d array:")
arr1 = np.array([1,2,3,4]) 
print(arr1)# one-dimension

print("\n2d array:")
arr2 = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(arr2)#two-dimension

print("\n3d array:")
arr3 = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print(arr3) # three-dimension

print("arr1 dim:", arr1.ndim)
print("arr2 dim:", arr2.ndim)
print("arr2 dim:", arr3.ndim)