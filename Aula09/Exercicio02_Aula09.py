import pandas as pd

df = pd.read_csv('C:/Temp/data2.csv')

x = df["Calories"].mean()
y = df["Maxpulse"].mean()

print(x)
print(y)

df.fillna({"Calories":x}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())