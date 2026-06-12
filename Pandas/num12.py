# random model in numpy:
"""
* rand() :- random float values
* randint() :- random integers
* randn() :- normal distribution
* choice() :- random selection
* shuffle() :- shuffle the original array
* permutation() :- shuffled copy
* seed() :- reproducible randomness.
"""

import numpy as np
print("\n printing random float values :", np.random.rand())
print("\n printing multiple random values :", np.random.rand(5))
print("\n printing random 2d array : ", np.random.rand(2,3)) 
print("\n printing random integer values:", np.random.randint(1,10)) #(start, end, size)--|
print("\n printing random multiple integer values:", np.random.randint(1,100,5)) #--------|
a = np.array([1,2,3,4,5,6])
print("\n printing random choice :", np.random.choice(a))
print("\n multiple random choice :", np.random.choice(a, size=4))
b= np.array([10,20,30,40,50,60])
np.random.shuffle(b)
print("\n modifing the original data :", b)

c= np.array([1,2,3,4])
new_c = np.random.permutation(c)
print("\n printing the permutation :")
print(c)
print(new_c)

print("\nfixed random integers:")
np.random.seed(1)
print(np.random.randint(1,100,5))

print("\n")
print(np.random.randn(5))

# random distrubution:
print("\n")
data = np.random.normal(
    loc = 50,
    scale = 10,
    size = 5
)
print(data)