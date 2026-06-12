# Merging and Joining data in pandas:
# sometimes data is stored in multiple coulmns. : like....
import pandas as pd
students = pd.DataFrame({
    "ID" : [1,2,3],
    "Name" : ["Rachith", "Kumar", "Rachi"]
})

marks = pd.DataFrame({
    "ID" : [1,2,3],
    "Marks" : [85,90,78]
})

print("\n",students)
print("\n", marks)

# * merge() ---------- used to combine dataframe based on common column:
result = pd.merge(students, marks, on="ID")
print("\n",result)

# there are 3 types of merging * left, right, outer megring:

#left merging : keeps all rows from left table
result1 = pd.merge(students, marks, on="ID", how="left")
print("\n", result1)

#right merging : keeps all rows from right table
result2 = pd.merge(students, marks, on="ID", how="right")
print("\n", result2)

#outer merging : keeps everything
result3 = pd.merge(students, marks, on="ID", how="outer") # union of both table
print("\n", result3)

# * join() --- used to join using index values
df1 = pd.DataFrame(
    {"Name" :["Rachtih", 'Kumar']},
    index=[1,2]     
)
df2 = pd.DataFrame(
    {"Marks" : [85,90]},
    index=[1,2]
    )
print("\n",df1.join(df2))

# we can also use concatenate ----- pd.concat([data1, data2])
# if you don't need this u can reset this :
#print(pd.concate([data1,data2], ignore_index=True))