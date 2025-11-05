import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simular coleta de temperatura por 5 dias
dias = np.arange(1, 6)  # gera [1, 2, 3, 4, 5]
temperaturas = np.round(np.random.uniform(15, 42, size=5), 1)  # gera 5 valores aleatórios

# Cálculos
media = np.mean(temperaturas)
maior = np.max(temperaturas)
dia_mais_quente = dias[np.argmax(temperaturas)]

# Exibição dos resultados no terminal
print(f"Temperaturas dos 5 dias: {temperaturas}")
print(f"Média das temperaturas: {media:.1f}°C")
print(f"Maior temperatura: {maior}°C (dia {dia_mais_quente})")

# Plot do gráfico
plt.figure(figsize=(10,5))
sns.barplot(x=dias, y=temperaturas, palette='grey')

# Linha da média
plt.axhline(media, color='red', linestyle='--', label=f'Média: {media:.1f}°C')

plt.title("Temperatura por dia (Simulação de 5 dias)")
plt.xlabel("Dias")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()
