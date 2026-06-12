"""import pandas as pd
\\\\data = {
    "Name" : ["rachtih", "kumar", "manu", "sam"],
    "Ages" : [20, 21, 19, 22],
    "Marks" : [85, 90, 78, 92],
    "City" : ["Delhi", "Mumbai", "Chennai", "Bangalore" ]
}
df = pd.DataFrame(data)
print(df)\\\\

# creating a series and data frames
"1d labeled array like a column in excel."
s = pd.Series([10,20,30,40])
print(s)

#customed index
sc = pd.Series([10,20,30,40], index=["a","b","c","d"])
print("\n", sc)

# wee can also make this by dictinory also.
d = { "a":100, "b":200, "c":300, "d":400}
df = pd.Series(d) #keys become index automaticaly.
print(df)

# asccessing the data:
print("\n\taccessing the data\n")
print(sc["a"]) # by index or same like list.


#dataframes : it is a 2d table  cantains: rows and columns
data = {
    "Name" : ["rachtih", "kumar", "manu", "sam"],
    "Ages" : [20, 21, 19, 22],
    "Marks" : [85, 90, 78, 92],
    "City" : ["Delhi", "Mumbai", "Chennai", "Bangalore" ]
}
df = pd.DataFrame(data)
print(df)

# creating by list:
data1 = [
    ["a", 20],
    ["b", 21],
    ["c", 34]
]
df1= pd.DataFrame(data1, columns=["Name", "Age"])
print(df1)

# also can custom index
df2 = pd.DataFrame(data1, columns=["Name", "Age"], index=["x","y","z"] )
print(df2)


#accessing data
"column access:"
print(df1["Name"])

"to access rows have use loc keyword :"
"having 2 ways: .loc for label and .iloc for posstion"
print(df.loc[0])   # by label
print(df.iloc[1])"""



"""introduction to pandas : used for data analysis, data manuplation, handling structure data
 """
"""creating series and datafarmes
              |            |
       ------------------------------
        |                           |
    series is a 1D        dataframes is a 2D array
    array.                (or) collection of series.
"""
import pandas as pd
print("series  :\n")
data1 = pd.Series([1,2,3,4])
print(data1)

print("dataframes : \n")
data2 = {
    "name" : ['rachith', 'kumar', 'vinay', 'sam'],
    "age" : [21, 20, 21, 20]
}
df = pd.DataFrame(data2)
print(df)