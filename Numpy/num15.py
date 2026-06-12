import numpy as np
arr = np.array([1,2,3,4,np.nan,6])
print(arr) # this is the missing value.
print("detecting the missing value:", np.isnan(arr))# shows where missnig values exit.
b = np.nan_to_num(arr)
print("replacing the missing value with zero:", b)

# when we calculating the mean for this  mean  while ignore this missiing value. normal mean fails with NaN.
print(np.nanmean(arr))

# normlization.
c =  np.array([10,20,30,40,50])
normlization = (c - c.min())/(c.max()-c.min())
print(normlization)

# standardized.
standardized = (
    c - np.mean(c)
) / np.std(c)
print(standardized)


# Image Processing with NumPy.



print("\n")
# student dataset analysis.
marks = np.array([45,67,89,90,34,76,99])

print("Average:", np.mean(marks))

print("Topper:", np.max(marks))

print("Passed Students:")
print(marks[marks >= 35])
