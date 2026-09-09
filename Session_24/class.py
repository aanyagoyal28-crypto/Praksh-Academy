import pandas as pd
df = pd.DataFrame({
    "date": ["2024-06-01", "2024-06-02", "2024-06-03"],
    "sales": [100, 150, 200]
})

print(df)
print(df.dtypes)

df["date"] = pd.to_datetime(df["date"])

print(df.dtypes)
#'01-06-2024' - dayfirst will not change the order of the date. It will just represent the date orders in the give date

df["date"] = pd.to_datetime(df["date"],dayfirst=True)

print(df["date"].dt.strftime('%d-%m-%Y'))
print(df["date"].dt.year)
print(df["date"].dt.month)
print(df["date"].dt.day)
print(df["date"].dt.quarter)
print(df["date"].dt.day_name)

# print(pd.to_datetime(df["date"],dayfirst=True))
'''
0-Sunday
6-Saturday  
'''
result=df.groupby(
    df["date"].dt.month
)["sales"].sum()

print(result)