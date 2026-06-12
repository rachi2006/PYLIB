# indexing and sliceing in numpy
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6, 7, 8])
b = np.array([
    [1,2,3],
    [4,5,6]
])
c = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

# indexing of the elements:
print("this is indexing of a : ", a[0]) #       |
print("this is indexing of b : ", b[1,2]) #     |----- this is normal sliceing. 
print("this is indexing of c : ", c[1,1,1]) #   |

# now by slicing:
print("sliceing of a :", a[1:3]) # row : column
print("slicing of b : ", b[0:2,1:3]) # row_slice, cloumn_sclice.

#now boolean indexing:
print(a[a>2])       #  |
#                      |--- like a conditions:  
print(a[a % 2 == 0]) # |


# by fancy indexing: -  selecting multiple elements by index
print(a[[0,2,4]])

a[1] = 100 # |---- modifing the array
print(a) #   


print(b[1, :])
