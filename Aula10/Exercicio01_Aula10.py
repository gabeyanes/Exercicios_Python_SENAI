import pandas as pd
import plotly.express as px

# ============================
# 1. Ler e preparar os dados
# ============================
arquivo = 'C:/Temp/venda.csv'
df = pd.read_csv(arquivo, sep=';')

# Limpar colunas extras
df = df[['VendasID', 'Vendedor', 'Cliente', 'Data', 'Produto', 'ValorUni', 'Quantidade']]

# Converter Data para datetime e calcular Ano
df['Data'] = pd.to_datetime(df['Data'], dayfirst=True, errors='coerce')
df['Ano'] = df['Data'].dt.year

# Calcular valor total
df['ValorTotal'] = df['ValorUni'] * df['Quantidade']

# ============================
# 2. Gráfico de Pizza por Vendedor
# ============================
vendas_por_vendedor = df.groupby('Vendedor')['ValorTotal'].sum().reset_index()
fig_vendedor = px.pie(vendas_por_vendedor, names='Vendedor', values='ValorTotal',
                      title='Participação Percentual das Vendas por Vendedor')
fig_vendedor.show()

# ============================
# 3. Gráfico de Pizza por Produto
# ============================
vendas_por_produto = df.groupby('Produto')['ValorTotal'].sum().reset_index()
fig_produto = px.pie(vendas_por_produto, names='Produto', values='ValorTotal',
                     title='Participação Percentual das Vendas por Produto')
fig_produto.show()

# ============================
# 4. Gráfico de Pizza por Ano
# ============================
vendas_por_ano = df.groupby('Ano')['ValorTotal'].sum().reset_index()
fig_ano = px.pie(vendas_por_ano, names='Ano', values='ValorTotal',
                 title='Participação Percentual das Vendas por Ano')
fig_ano.show()