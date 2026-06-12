"""
data selection and filtering:
selection : means choosing specfic rows or cloumns
filtering : means showing the data that matches certian condition.
"""
import pandas as pd
data = {
    "Name" : ['rachith', 'kumar', 'vinay', 'sam'],
    "Age" : [20, 21, 20, 22],
    "marks" : [85,90,78,92],
    "City" : ['delhi', 'mumbai', 'chennai', 'odisha']
}
df = pd.DataFrame(data)
print(df)

#single conditioin filtering:
print("\n", df[df["marks"] > 80])
 # filter by age:
print("\n", df[df["Age"] >= 21])


print("\n", df[(df["marks"] > 80) & (df["Age"] > 20)]) # AND
print("\n", df[(df["marks"] > 80) | (df["Age"] > 20)]) # OR
print("\n", df[~(df["City"] == "delhi")]) #NOT


#seleting specfic column after filtering
#print("\n", df[df["Marks"] > 80][["Name", "Marks"]])


#"""#isin()-- used to match multiple values.
print("\n",df[df["City"].isin(["delhi", "mumbai"])]) 
"""
import pandas as pd
data = {
    "Name" : ['rachith', 'kumar', 'vinay', 'sam'],
    "Age" : [20, 21, 20, 22],
    "marks" : [85,90,78,92],
    "City" : ['delhi', 'mumbai', 'chennai', 'odisha']
}
df = pd.DataFrame(data)
df["Age"] = df["Age"].astype(float)
print(df[df["City"].isin(["delhi", "mumbai"])])

"""