import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
import numpy as np

df = pd.read_csv('C:/Temp/data4.csv', sep=',', header=0)

print(len(df.columns))

df.columns = [
    'Data',
    'Preço',
    'Quartos',
    'Banheiros',
    'Area_construida',
    'Tamanho_lote',
    'Andares',
    'Fonte_Agua',
    'Vista',
    'Condição',
    'Area_teto',
    'Area_Porão',
    'Ano_Construido',
    'Ano_Renovação',
    'Rua',
    'Cidade',
    'CEP',
    'Pais'
]

df['Preço'] = df['Preço'].apply(lambda x: round(x, 2))

print(df.to_string())
print(df.dtypes)

df = df.drop(columns=['CEP', 'Fonte_Agua', 'Area_Porão', 'Area_teto', 'Rua', 'Cidade', 'Pais', 'Data'])

corr = df.corr(numeric_only=True)

print(corr)

# Remover linhas com valores nulos
df = df.dropna()

# Selecionar as variáveis (X = independente, y = dependente)
x = df[['Area_construida']]   # variável explicativa
y = df['Preço']               # variável alvo

# Criar o modelo
modelo = LinearRegression()

# Treinar o modelo
modelo.fit(x, y)

# Fazer previsões
y_pred = modelo.predict(x)

# Plotar o gráfico
plt.figure(figsize=(12, 6))
plt.scatter(x, y, color='blue', label='Dados reais')
plt.plot(x, y_pred, color='red', label='Regressão Linear')
plt.xlabel('Área construída')
plt.ylabel('Preço')
plt.grid()
plt.title('Regressão Linear - Preço vs Área construída')
plt.legend()
plt.show()
