# NumPy Internals & Expert-Level Optimization

# strides: Strides tell NumPy:
#How many bytes to move in memory to access next element.
import numpy as np
a = np.array([
    [1,2,3],
    [4,5,6]
])
print(a.strides)
"""
Explanation
For int64:
Each value = 8 bytes
Meaning:
Move 8 bytes for next column
Move 24 bytes for next row
"""

# vectorized execution means:
#Entire array processed at once.
e = np.arange(1000000)

result = e * 2

"""
Performance Difference
NumPy operations can be:
50x to 100x faster
than Python loops.
"""

# in-phase operation : Operations modifying same memory.
f = np.array([1,2,3])
f += 5
print(f)
"""
Explanation
Uses same memory instead of creating new array.
Efficient for:
Large datasets
Memory optimization
"""
#Check Memory Flags
print(a.flags)
"""
Explanation
Shows:
Memory layout
Ownership
Write permissions
"""