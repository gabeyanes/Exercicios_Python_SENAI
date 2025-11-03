# SIMULAR A COLETA DE TEMPERATURA POR 5 DIAS.
# ARMAZENAR EM ARRAY
# CALCULAR A MÉDIA E IDENTIFICAR O DIA MAIS QUENTE
import numpy as np

temperaturas = np.array([])

print("Iremos fazer a análise das temperaturas durante 5 dias, por favor comece a inserir as temperaturas dos dias: ")

for i in range(5):
    valordatemperatura = float(input(f'Insira a {i+1}° temperatura: '))
    temperaturas = np.append(temperaturas ,valordatemperatura)
    

media = np.mean(temperaturas)
maior = np.max(temperaturas)

print(f'está são as temperaturas dos 5 dias: {temperaturas}')
print(f'está é a média das temperaturas: {media}')
print(f'está é a maior temperatura: {maior}')