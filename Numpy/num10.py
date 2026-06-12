# boardcasting in numpy
import numpy as np
a = np.array([1,2,3,4])
print(a + 2)  # numpy automatically treat 2 as [2,2,2,2] know as boadcasting


#boadcasting bewteen array
b = np.array([5,6,7,8])
print(a+b)    # element wise addition

# boadcasting with different shapes
c = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

d = np.array([10,11,12,13]) # numpy automatically expand b. 

print(c+d)