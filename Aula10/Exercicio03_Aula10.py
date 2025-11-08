import matplotlib.pyplot as plt
from skylearn.linear_model import LinearRegression
import numpy as np

# Dados de exemplo
x = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# Criar e treinar o modelo de regressão
modelo = LinearRegression()
modelo.fit(x,y)

y_pred = modelo.predict(x)

plt.scatter(x, y, color='blue', label='Dados reais')

plt.plot(x, y_pred, color='red', linewidth=4, label='Regressão Linear')

# Personaliar o gráfico

plt.title('Dispersão com Regressão Linear')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
