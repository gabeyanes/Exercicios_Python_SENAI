import pandas as pd

df = pd.read_csv('C:/Temp/data2.csv')

x = df["Calories"].mean()
y = df["Maxpulse"].mean()

print(x)
print(y)

df.fillna({"Calories":x}, inplace=True)

df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace = True)

print(df.to_string())