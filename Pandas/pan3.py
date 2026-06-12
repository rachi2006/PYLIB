"""
data Clening in pandas:
means fixing incorect data, handling missing values, removing duplicates, correcting data types
"""

import pandas as pd
import numpy as np
data = {
    "Name" : ["rachith", "vinay", "kumar", "sam"],
    "Age" : [20, np.nan, 19, 21],
    "Marks" : [85, 90, np.nan, 85],
    "City" : ["delhi", "mumbai", "chennai","delhi"]
}
df = pd.DataFrame(data)
print(df)

#to know the values are missing the data use isnull()
print("\n", df.isnull()) # if the value is missing this will print true else flase.

print("\nnumber of missing value", df.isnull().sum()) # count missing value.

print("\nremoving the missing value", df.dropna()) # this remove the row which containing missing values.
#if u want to remove column which contain missing value use dropna(axis=1)

print("\nfilling the missing values :", df["Age"].fillna(18))
# we can also fill by mean also like (df["Marks"].mean(), inplace=True)

# duplicate data
print(" showing duplicate data is present or not :", df.duplicated()) # it shows only if 2 rows having same data.
# to remove that df.drop_duplicate(inplace=true)

print("\n renameing the columns:", df.rename(columns={"Marks":"Score"}, inplace=True))
print(df.dtypes)
#converting the data type.
"""print(df["Age"]=df["Age"].astype(int))"""
#to replace the value
print("\n", df["City"].replace("delhi", "NewDelhi"))

#rempove the column;
df.drop("City", axis=1, inplace=True)
print(df)