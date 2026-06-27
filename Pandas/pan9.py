# Time series data in pandas
#:- data collected over time intervals is called time series data.
#  It is a sequence of data points collected or recorded at specific time intervals. 
# Time series data can be used for various purposes, such as forecasting, trend analysis, and anomaly detection.
#Examples:
# Daily stock prices
# Temperature every hour
# Monthly sales
# Website visitors per day

import pandas as pd
# Create a time series data using date range
data = {
    "date": ["2023-01-01",
             "2023-01-02",
            "2023-01-03", 
            "2023-01-04", 
            "2023-01-05"],
    "sales": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
print("Time Series Data:")
print(df) 

# converting string to date
# initially :-
print("\nData types before conversion:" , df.dtypes)
#problem :-
# date is a string(object), nota real data,
#converting it
df["date"] = pd.to_datetime(df["date"])
print("\nData types after conversion:" , df.dtypes)


# set date as index:
# time series ooften uses data ass index:
df.set_index("date", inplace=True)
print("\nTime Series Data with Date as Index:")
print(df)

# access date by date
print("\nAccessing data for a specific date:", df.loc["2023-01-01"])

#get date range
print(df.loc["2023-01-01":"2023-01-03"])


# extract parts of date
print("\nYear:", df.index.year)
print("Month:", df.index.month)
print("Day:", df.index.day)

#generate date range
# it create a dates automatically:
dates = pd.date_range(
    start="2023-01-01",
    periods=5
)
print(dates)

#With monthly intervals:

dates11 = pd.date_range(
    start="2026-01",
    periods=5,
    freq="ME"
)
print(dates11)

# rolling average
#used in stockanalysis, weather analyisi, trends
df["moving_avg"]= (
    df["sales"].rolling(3).mean()
)
print(df)