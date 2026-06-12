import numpy as np 
#operations on numpy 
arr = np.array([1,2,3,4]) 
print(arr + 2) # add 2 to each elements. [3 4 5 6]        |
#                                                         |-- this is called vectorization
print(arr * 2) # multiply 2 to each elements. [2 4 6 8]   |

arr2 = np.zeros(3)
print(arr2)

arr3 = np.ones(6)
print(arr3)

print("arr3:", np.arange(1,6+1)) # like python range()

print("arr4:", np.linspace(0,1,5)) #fixed number of values b/w start and step

print("arr5 :", np.eye(3)) #identity matrix

print("arr6 :", np.random.rand(3)) # random elements, defualtly float
print("arr7 :", np.random.randint(4)) # random int elements

# we can also create a array with datatype
arr8 = np.array([1,2,3], dtype=float)
print("arr8:",arr8)

# array attributes and properties in numpy
"""
* shape (rows, columns)
* ndim - it show the dimensioin of array
* size - it show the no. of rows and columns
* dtype - it show that type of data stored in array
* itemsize - memory usedd by the elements(how many bytes each elements occupies)
"""
import numpy as np
a = np.array([1.2 ,2.134 ,3.7 ])
b = np.array([
    [1,2,3],
    [4,5,6]
])
c = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
print("this is shape of array :", a.shape, b.shape, c.shape)
print("this is dim of array :", a.ndim, b.ndim, c.ndim)
print("this is size of array:", a.size, b.size, c.size)
print("this is data type of elements: ", a.dtype, b.dtype, c.dtype)
print("itemsize of arrays: ", a.itemsize, b.itemsize, c.itemsize)
print(len(b), np.size(b))
print("bsdk")