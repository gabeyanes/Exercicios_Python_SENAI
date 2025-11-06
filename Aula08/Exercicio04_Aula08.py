import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Temp/data1.csv')

print(f'\n\nPrimeira Planilha sem alterações \n\n {df.to_string()}')

x = round(df["Calories"].mean(),2)

print(f'\n\nMédia \n{x}')

df.fillna({"Calories":x},inplace = True)

print(f'\n\nValores substituidos \n\n {df.to_string()}')

plt.figure(figsize=(12,6))
plt.hist(df["Calories"], bins=10, color='skyblue', edgecolor='red')
plt.title("Duração X Calorias")       # Título
plt.xlabel("Calorias")                 # Eixo X
plt.ylabel("Duração")                  # Eixo Y
plt.grid(True, linestyle='--', alpha=1)
plt.show()