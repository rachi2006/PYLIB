# datafram basics *****
""" create a simple datafram"""
import pandas as pd
data = {
    "Name" : ['rachith', 'kumar', 'vinay', 'sam'],
    "Age" : [20, 21, 20, 22],
    "marks" : [85,90,78,92],
    "City" : ['delhi', 'mumbai', 'chennai', 'odisha']
}
df = pd.DataFrame(data)
print(df)

# viewing the data :
# head()---- is used to show the first rows  defult : 5 rows
print("\nview the data by head() : \n", df.head())

# for specific rows use (head(2)) determine the  value to view
print("\n for spectic row :\n", df.head(2))

# tail() shows last rows:
print("\nview the data by tail : \n", df.tail())

# for specific rows use (head(2)) determine the  value to view
print("\n for spectic row :\n", df.tail(2))

#understanding the index:
"""index = row labels."""
print("\n current index :", df.index)

# we can also custom th index
print("\n customizing the index to 0,1,2,3 --- a,b,c,d,")
df.index = ['a','b','c','d']
print(df)

# understanding the column 
#get column name
print("\n getting the current column:")
print(df.columns)

# we can add a new column to data
print("\nadding a new column to data :")
df["grade"] = ["A","A","b","A+"]
print(df)

#now deleting the column :
print("\ndeleting the column :")
print(df.drop("grade", axis=1, inplace=True))
print(df)


# selecting the column
print("selecting the single column :\n", df["Name"])
print("\n selecting the multiple column:", df[["Name", "Age"]])

#selecting rows:
print("selecting the single row :\n", df.loc["a"])
print("\n selecting the multiple row:", df.loc[["a", "b"]])
# selecting both row and column:
print("\nselecting row and column:", df.loc["a","marks"])

# selecting the rows by iloc() -- position based selection.
print("\nselecting row by using iloc() :", df.iloc[0])
print("\nselecting multiple row by using iloc() :", df.iloc[0:2])

#shape,size, info:
print("\nshape of a data:", df.shape)
print("\n information of the data:", df.info())
print(df.describe())