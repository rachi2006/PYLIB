"""
 grouping and Aggregation in pandas:
 grouping means : dividind the data into based on some categores
 aggregation means : performing calcilation on each group

"""
import pandas as pd
data = {
    "Name" : ["Ravi", "Anu", "kiran", "Meena", "Rahul", "priya"],
    "City" : ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi", "Mumbai"],
    "Marks" : [85, 90, 78, 92, 88, 95]
}
df = pd.DataFrame(data)

# groupby() ----- df.groupby("column")
print(df.groupby("City"))

#calculate sum ---- finding totol sum for each city.
print("\nfinding totol sum for each city :.\n", df.groupby("City")["Marks"].sum())

#calculatinf mean()
print("\ncalculatinf mean() :\n")
print(df.groupby("City")["Marks"].mean())

#count values
print("\ncount values :\n")
print(df.groupby("City")["Marks"].count())

#count values
print("\ncount values :\n")
print(df.groupby("City")["Marks"].max())
#minimum values
print("\nminimum values :\n")
print(df.groupby("City")["Marks"].min())


# multiple aggregation using agg() funcation.
# instead of writing many function seperately do like this 
print("\nmultiple aggregation using agg() funcation :\n")
print(df.groupby("City")["Marks"].agg(["sum", "mean", "max", "min"]))

# group by multiple columns:
data2 = {
    "City" : ["Delhi", "Delhi", "Mumbai", "Mumbai"],
    "Gender" : ["Male","Femal", "Male", "Femal"],
    "Marks" : [85, 90, 78, 92]
}
df2 = pd.DataFrame(data2)                                                                #--------------
print("\nthis is multiple group by  :\n", df2.groupby(["City", "Gender"])["Marks"].mean().astype(int))# |--- optional based on your skills/ use your skills here
                                                                                         # --------------


# if know  don't need this methodes but u need that previous data: used reset_inden()
grouped = df.groupby("City")["Marks"].mean()  
print(grouped)                                                                                  

print("\nreseting the data :\n", grouped.reset_index())

# size() vs count()
#size () --- count all rows.
#count() --- count non missing values.

print("\n ", df.groupby("City")["Marks"].count())
print("\n ", df.groupby("City")["Marks"].size())