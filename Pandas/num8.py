# iterating over the array:-
# we can use loop like normal iteration, nested loops
# but it provide tools like nditer(), ndenumerate()S

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

#iterating in 1d array:
print("iterating in 1d aray :")
for x in a:    # loop take 1 element at a time.
    print(x)


#iterating in 2d array:                     #  |
print("\niterating in 2d array :")          #  |
for row in b:                               #  |----- each iteration return one row.
    for element in row:                     #  |
        print(element)                      #  |


# iterating in 3d array:
print("iterating in 3d array :")
for block in c:
    for row in block:
        for element in row:
            print(element)



# using tools :
print("\n iteration by using tool: np.nditer() in 2d : ")
for x in np.nditer(b):
    print(x)


print("\n iteration by using tool: np.nditer() in 3d : ")
for x in np.nditer(c):
    print(x)


# we can also modify the array during iteration like converting int to float:       #
for x in np.nditer(a, flags=["buffered"], op_dtypes=['S']):                         #--- conveting integer into string bytes during iteration
    print(x)                                                                        #

print("\n iterating with step size : ")    # 
for x in np.nditer(b[:, ::2]):             #---  ::2 this take every second column
    print(x)                               #


print("\n iteration by using tool: np.ndenumerate() in 1d ")          #
for index, value in np.ndenumerate(a):                                # ----------  it returns index position and values
    print(index, value)                                               #

print("\n iteration by using tool: np.ndenumerate() in 2d ")          #
for index, value in np.ndenumerate(b):                                # ----------  it returns index position and values
    print(index, value)  
