import pandas as pd

df = pd.read_csv('C:/Temp/data1.csv')

print(f'\n\nPrimeira Planilha sem alterações \n\n {df.to_string()}')

x = round(df["Calories"].median(),2)

print(f'\n\nMediana \n{x}')

df.fillna({"Calories":x},inplace = True)

print(f'\n\nValores substituidos \n\n {df.to_string()}')