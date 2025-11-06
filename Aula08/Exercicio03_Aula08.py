import pandas as pd

df = pd.read_csv('C:/Temp/data1.csv')

print(df.to_string())

x = df.dropna()

print(x.to_string())