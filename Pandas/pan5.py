"""
***** Data manipulation in pandas*****.
means : modifing the data, sorting, changing, 
for examples : sorting students by marks, adding bouns morks, converting names to uppercase, rank students 

"""

import pandas as pd
data = {
    "Name" : ["Rachith", "Vinay", "Kumar", "Rachi"],
    "Marks" : [90, 91, 89, 75],
    "City" : ['delhi', 'mumbai', 'chennai', 'odisha']
}
df = pd.DataFrame(data)
print(df)

# * we will sort a data ----+
#                           |---------- Ascending order.
#                           |-----------Descending order.

#printing ascending order
print("\nascending order :\n", df.sort_values("Marks")) #defult ascending order
print("\ndescending order :\n", df.sort_values("Marks", ascending=False))


# sorting multiple columns
print("\nsorting multiple columns :\n", df.sort_values(["City", "Marks"]))

"""# modifing the coulmns values:
print("\nadding +5 marks to each students")
df["Marks"] = df["Marks"] + 5
print(df)"""

#creating new coulmn
df["Bouns"] = 5
print(df)

"""# using apply() ---- applying a function to value.
# for example:
print("\n showinf to apply apply() function")
df["Marks"] = df["Marks"].apply(
    lambda x:x*2
)
print(df)"""

print("\n converting names to upper case :\n")
df["Name"] = df["Name"].apply(
    lambda x: x.upper()
)
print(df)


#map() -- transforms values
print("\n using map() function\n")
grades = {
    75 : "B",
    89 : "B+",
    90 : "A",
    91 : "A+"
}
df["Grades"] = df["Marks"].map(grades)
print(df)

# ranking the data: assign the ranks
print("\n ranks of marks: \n")
df["Ranks"] = df["Marks"].rank()
print(df) # it shows who having less marks has less rank, for grater marks highest rank.
df["Ranks"] = df["Marks"].rank(ascending=False)
print(df) # for ranks like compitative exames.


# we already used replace() function

# using where() --- conditions
print(df["Marks"].where(df["Marks"] > 80)) # the values <= 80 become NAN.
 

# using mask() ---- opposite to where()
print(df["Marks"].mask(df["Marks"] > 80)) # > 80 becomes NAN