import pandas as pd

df = pd.read_csv('C:/Temp/datacor.csv')

# CORRELAÇÃO ENTRE COLUNAS PARA MELHOR CRIAÇÃO DE GRÁFICOS

print(df.corr())