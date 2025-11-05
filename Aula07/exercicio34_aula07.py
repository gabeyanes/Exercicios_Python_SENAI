import pandas as pd

df = pd.read_json('C:\Temp\data.json')

df_ordenado = df.sort_values(by='Calories', ascending=False)

print(df_ordenado)
print(df.tail())
print(df.head(10))
print(df.to_string())
