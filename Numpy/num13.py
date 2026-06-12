# numpy file handling:
"""
* save() :- save numpy array.
* load() :- load saved array.
* savetxt() :- save as txt or csv
* loadtxt() :- load text or csv.
* npy files :- numpy binary formate.
"""

import numpy as np
arr = np.array([1,2,3,4,5])
np.save("1darray", arr)

data = np.load("1darray.npy")
print(data)

#saving 2d array:
a = np.array([
    [1,2,3],
    [4,5,6]
])

np.save("2darray", a)
data2 = np.load("2darray.npy")
print(data2)

# saving as a txt file:
np.savetxt("txtfile.txt", a)
np.savetxt("txtfile.csv", a, delimiter=",") # saving as csv file

#loading txt file and csv file:
data3 = np.loadtxt("txtfile.txt")
data4 = np.loadtxt("txtfile.csv", delimiter=",")


print("\n", data3)
print("\n", data4)


# we can also save multiple array 
np.savez("multiarray", first=arr, second=a)
data5 = np.load("multiarray.npz")
print(data5["first"])
print(data5["second"])