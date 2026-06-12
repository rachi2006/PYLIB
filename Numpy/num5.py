# mathematical operations in numpy.
"""
* arithmetic operations.
* aggregation function :-  combine many values into single value
"""
import numpy as np
a = np.array([1,2,3,4,5,6])
t = np.array([7,8,9,10,11,12])
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

print(a+t)  # addition
print(a-t) # subtraction
print(a*t) # multiplication
print(a/t) # division
print(a % t) # modulus
print(a**2) # power


print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))
print(np.std(a))

# now this operations on 2d arrays:
print(np.sum(b, axis=0)) # colums-wise operation. 
print(np.sum(b, axis=1)) # row-wise operation.

# builtin mathematical function.
print(np.sqrt(a))
print(np.exp(a))
print(np.sin(a))
print(np.cos(b))