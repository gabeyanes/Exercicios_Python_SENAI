# SIMULAR A COLETA DE TEMPERATURA POR 5 DIAS.
# ARMAZENAR EM ARRAY
# CALCULAR A MÉDIA E IDENTIFICAR O DIA MAIS QUENTE
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dias = np.array([])
temperaturas = np.array([])

print("Iremos fazer a análise das temperaturas durante 1 mês, por favor comece a inserir as temperaturas dos dias: ")

for i in range(31):
    valordatemperatura = np.random.uniform(15,42)
    valordatemperatura = np.round(valordatemperatura,1)
    temperaturas = np.append(temperaturas ,valordatemperatura)
    temperaturas = np.round(temperaturas,1)
#     temperaturas = np.sort(temperaturas)
    dias = np.append(dias, i+1)
    dias = dias.astype(int)

plt.figure(figsize=(24,6))
ax = sns.barplot(x=dias, y=temperaturas)

# Colocar valores dentro das barras com estilização
for i, temp in enumerate(temperaturas):
    ax.text(i, temp - 1, f'{temp}°C',    # texto
            ha='center',                 # horizontal center
            va='top',                 # vertical center dentro da barra
            fontsize=12,                 # tamanho da fonte
            fontweight='bold',           # negrito
            color='white')               # cor do texto
    
plt.title("Temperatura por dia")
plt.xlabel("Dia")
plt.ylabel("Temperatura (°C)")
    
media = np.mean(temperaturas)
maior = np.max(temperaturas)

print(f'está são as temperaturas dos 5 dias: {temperaturas}')
print(f'está é a média das temperaturas: {media}')
print(f'está é a maior temperatura: {maior}')

plt.show()

