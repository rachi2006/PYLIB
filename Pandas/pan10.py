#pivot table and reshaping data
#What is Pivoting & Reshaping?
#Sometimes data is not arranged in the format we need.
#We may want to:
#summarize data
#rearrange rows and columns
#convert wide data ↔ long data
#Pandas provides tools for this:
#pivot_table()
#melt()
#stack()
#unstack()

import pandas as pd

data = {
    "Name":["Ravi","Ravi","Anu","Anu"],
    "Subject":["Math","Science","Math","Science"],
    "Marks":[85,90,88,95]
}

df = pd.DataFrame(data)

print(df)

#1. Pivot Table
#pivot table summarizes data into a new structure.
pivot =df.pivot_table(
    values="Marks",
    index="Name",
    columns="Subject"
)
print(pivot)
"""
Understanding

Original:

Ravi  Math      85
Ravi  Science   90
Anu   Math      88
Anu   Science   95

After pivot:

          Math   Science
Ravi       85       90
Anu         88       95

Rows become organized into a summary table."""

#2.pivot with aggregation: if dupicate values exist.
pivot2 = df.pivot_table(
    values="Marks",
    index="Name",
    columns="Subject",
    aggfunc="mean"
)

print("\n", pivot2)

#3. Multiple Aggregations
pivot3 = df.pivot_table(
    values="Marks",
    index="Name",
    columns="Subject",
    aggfunc=["mean","max"]
)

print("\n", pivot3)

"""
4. melt() (Wide → Long)

melt() converts multiple columns into rows.

Example:

data = {
    "Name":["Ravi","Anu"],
    "Math":[85,88],
    "Science":[90,95]
}

df = pd.DataFrame(data)

print(df)

Output:

    Name   Math   Science
0   Ravi     85      90
1    Anu     88      95

Apply melt:

melted = pd.melt(
    df,
    id_vars=["Name"],
    var_name="Subject",
    value_name="Marks"
)

print(melted)

Output:

    Name   Subject    Marks
0   Ravi     Math        85
1    Anu     Math        88
2   Ravi   Science       90
3    Anu   Science       95
📌 Meaning

Before:

Math      Science
85           90
88           95

After:

Subject      Marks
Math            85
Science         90

Columns become rows."""

"""
5. stack()

Converts columns into row indexes.

Example:

df = pd.DataFrame({
    "Math":[85,88],
    "Science":[90,95]
},
index=["Ravi","Anu"])

print(df)

Output:

        Math   Science
Ravi      85      90
Anu        88      95

Apply stack:

print(df.stack())

Output:

Ravi  Math       85
       Science   90
Anu   Math       88
       Science   95
🔹 6. unstack()

Opposite of stack.

print(
    df.stack().unstack()
)

Output:

        Math   Science
Ravi      85      90
Anu        88      95
📌 Relationship
stack()
      ↓
Rows increase
Columns decrease

unstack()
      ↓
Columns increase
Rows decrease"""