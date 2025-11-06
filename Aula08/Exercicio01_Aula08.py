import pandas as pd

df = pd.read_csv('C:/Temp/data.csv')

print(df.to_string())

#VAI ALOCAR O VALOR MÉDIO
x = df["Calories"].mean()

print('\n\nMédia',x,'\n\n')

y = df["Calories"].median()

print('\n\nMediana',y,'\n\n')

df.fillna({"Calories":x}, inplace = True)

print(df.to_string())
