# statistical function in numpy
"""

"""
import numpy as np
a = np.array([1,2,3,4,5])
a1 = np.array([1,50,100])

# to find the average value of all :- mean()
# middle element of array :- median()

print("average (mean) of a : ", np.mean(a))
print("median of a : ", np.median(a)) # here median affected by outliers for example:-

b = np.array([10,20,30,1000]) # 1000 changes the mean heavily, mean remains stable
print("mean of b : ", np.mean(b))
print("median of b : ", np.median(b))

# standard deviation :-
print("std of a : ", np.std(a)) # low std for colse values like a contains
print("std of a : ", np.std(a1)) # values are spread widely - high std

#variance it measure the spread of data. std = square root of variance.
print("variance of a : ", np.var(a))

#min() and max()
print("min of a :", np.min(a))
print("max of a :", np.max(a))

#percentile :- what percentile of data falls below a value
print("percentile of a : ", np.percentile(a, 5))

# correlation :- corrcoef() - measures relationship between two dataset. 
# 1 - perfect +ve value, 0 - no relation, -1 - perfect -ve relation
x = np.array([1,2,3,4,5])
y = np.array([2,4,6,8,10])
print(np.corrcoef(x,y)) # as x increases, y also increases perfectily so corraltion = 1

b1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

print(np.mean(b1, axis=0)) # column wise
print(np.mean(b1, axis=1))# row wise