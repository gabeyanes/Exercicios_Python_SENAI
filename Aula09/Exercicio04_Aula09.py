import pandas as pd

df = pd.read_csv('C:/Temp/data2.csv')

x = df["Calories"].mean()
y = df["Maxpulse"].mean()
z = df["Duration"].mean()
print(x)
print(y)

df.fillna({"Calories":x}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace = True)
df.loc[7,'Duration'] = round(z)
df['Date'] = df['Date'].dt.strftime('%d/%m/%Y')

df.drop_duplicates(inplace = True)

print(df.duplicated())
print(df.to_string())