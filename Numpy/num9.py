# copy vs view in numpy
# copy() :- change in original do not affect copy of original. create completly independent array
#view():- change in original affected in copy.

import numpy as np
a = np.array([1,2,3])    #
b=a                      #
b[0] = 100               #------ does not create new array both variable point to same memory
print(a)                 #
print(b)                 #

print("\n by using copy() : ")
a1 = np.array([1,2,3,4])           #
b1 = a1.copy()                     #
b1[0] = 100                        #--------- copy creates a seperate memory
print(a1)                          #
print(b1)                          #



print("\n by view() : ")
a2 = np.array([1,2,3,4,5])         #
b2 = a2.view()                     #
b2[0] = 100                        #------------- both shares same memory.
print(a2)                          #
print(b2)                          #


# checking the base attribute : numpy provides  .base to check memory ownership.
print("\n base attribute of b1 : ", b1.base)    # none means * independent memory, real copy.
print("\n base attribute of b2 : ", b2.base) # it shows original array because memory is shared.


# even, slicing also creates views
print("\n")
a3 = np.array([1,2,3,4])
b3 = a3[1:3]
b[0] = 10
print(a)

# making slicing safe copy()
print("\n")
a4 = np.array([1,2,3,4])
b4 = a4[1:3].copy()
b4[0] = 100
print(a4)
print(b4)