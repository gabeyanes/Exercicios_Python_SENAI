import matplotlib.pyplot as plt
import numpy as np

y = np.array([])

for i in range(1,5):
    valor = np.random.uniform(10,100)
    valor = np.round(valor, 1)
    y = np.append(y, valor)
    y = np.round(y, 1)
    y = y.astype(int)
    
    
labels = ["Categoria A", "Categoria B", "Categoria C","Categoria D"]

print(y)
print(labels)

plt.pie(y, labels = labels, startangle=90)
plt.title("Distribuição de Categoria")
plt.axis('equal')
plt.show()

