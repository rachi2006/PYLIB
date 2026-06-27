# string operation in pandas
"""
What are String Operations?

String operations are used when columns contain text data.

Examples:

Convert names to uppercase
Remove extra spaces
Find words
Replace text
Split text
Extract specific characters

Pandas provides:
.str
The .str accessor allows string functions on DataFrame columns."""

import pandas as pd

data = {
    "Name":[" Ravi ","ANU","kiran","Meena"],
    "Email":[
        "ravi@gmail.com",
        "anu@yahoo.com",
        "kiran@gmail.com",
        "meena@yahoo.com"
    ]
}

df = pd.DataFrame(data)

print(df)

#convert to lowercase
print(df["Name"].str.lower())
print(df["Name"].str.upper())

# capitalize first letter
print(df["Name"].str.capitalize())

#remove extra space: somtimes datasets contain space:
# like : " ravi "
print(df["Name"].str.strip())
"""
Space Removal Functions
Function	Purpose
strip()	remove both sides
lstrip()	remove left side
rstrip()	remove right side"""

#find text using contains()
print(df["Name"].str.contains("a"))
"""6. Starts With
print(
    df[
        df["Name"]
        .str.startswith("R")
    ]
)

Output:

Ravi"""
"""8. Replace Text

Replace "gmail" with "outlook":

df["Email"] = (
    df["Email"]
    .str.replace(
        "gmail",
        "outlook"
    )
)

print(df)

Output:

ravi@outlook.com"""

#split strings
print(
    df["Email"]
    .str.split("@")
)
#store the split values in a new column
df[["Username","Domain"]] = (
    df["Email"]
    .str.split(
        "@",
        expand=True
    )
)

print(df)
"""10. Get Length of Text
print(
    df["Name"]
    .str.len()
)

Output:

0     7
1     3
2     6
3     6"""