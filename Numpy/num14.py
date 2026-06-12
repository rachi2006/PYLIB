# advence nupy concept:
""" 
* 
"""


import numpy as np
data = np.array([
    ("ravi", 21, 85.5),
    ("rachith", 20, 91.0)
], dtype=[
    ("name", "U10"),
    ("age", "i4"),
    ("marks", "f4")
])

print(data)

#accesss file:
print("\n", data["name"])