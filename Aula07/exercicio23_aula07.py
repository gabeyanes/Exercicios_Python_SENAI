import random
import matplotlib.pyplot as plt

# Simular coleta de temperatura por 5 dias
temperaturas = []
for dia in range(1,6):
    temp = round(random.uniform(10.0,37.0), 1) # Temperaturas entre 10°C a 37°C.
    temperaturas.append(temp)
    print(f'Dia {dia}: {temp}°C')
# Calcular média das temperaturas
media = sum(temperaturas)/ len(temperaturas)
print(f'\nMédia de temperaturas : {media:.1f}°C')

# Identificar o dia mais quente

dias_mais_quente = temperaturas.index(max(temperaturas)) + 1
print(f'Dias mais quente: Dia {dias_mais_quente} com {max(temperaturas)}°C')

# Gerar gráfico de Barras

dias = [f'Dia {i}' for i in range(1,6)]
plt.figure(figsize=(10,5))
plt.bar(dias, temperaturas, color= 'grey')
plt.title('Temperaturas por Dia')
plt.xlabel('Dias')
plt.ylabel('Temperatura (°C)')
plt.axhline(media, color='red', linestyle='--', label=f'Média: {media:.1f}°C')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

