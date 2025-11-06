import pandas as pd

df = pd.read_csv('C:/Temp/venda.csv', sep=';', usecols=lambda c: not c.startswith('Unnamed'))

# CORREÇÕES DE DATA

df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')

# CORREÇÃO DE VALORES

df['ValorUni'] = pd.to_numeric(df['ValorUni'], errors='coerce')
df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors='coerce')

print("Verificar se tem dados nulos\n")
print(df.isnull().sum(),"\n")

print("Verificar se tem dados duplicados\n")
print(df.duplicated().to_string(),"\n")

print("Tabela corrigida\n")
print(df.to_string(),"\n")

print(df.dtypes)

print(df.corr(numeric_only=True))
