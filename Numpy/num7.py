# Array joining & splitting in numpy
"""
concatenationi :- joining the array
"""
import numpy as np
a = np.array([1,2,3,4,5,6])
a1 = np.array([7,8,9,10,11,12])
b = np.array([
    [1,2,3],
    [4,5,6]
])

b1 = np.array([
    [7,8,9],
    [10,11,12]
])
c = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(" joining the two arrays :", np.concatenate((a,a1))) #joining thw 2 arrays.

# now concatenating 2d arrays but both array should be same dimension.
print("joining 2d arrays :\n", np.concatenate((b,b1)))

#now concatenating with axis.
print("this is row-wise concatenation with axix=0\n :", np.concatenate((b,b1), axis=0))
print("this is column-wise concatenation with axix=1\n :", np.concatenate((b,b1), axis=1))

# visual understanding :-   axis=0 is vertical and 1 is horizontal this are shortcut of concatenations:
# for vertical - vstack(), and horizontal - hstack()
print("vertical stack :\n ", np.vstack((a,a1)))
print("horizontal stack :\n", np.hstack((a,a1)))

#split() - used to split the into equal parts:
print("splitting the array :\n", np.split(a,3))

#array_split() - know as flexible splitting used if equal division is not impossible
print("splitting the  array into unequal :\n", np.array_split(a,4))

#spiltting 2d array:
print("splitting 2d array :\n", np.split(a,2))

arr = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print("splitting 2d array :\n", np.hsplit(arr,2))