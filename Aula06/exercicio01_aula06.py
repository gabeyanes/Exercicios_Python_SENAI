# CRIE UMA MATRIZ COM 5 DIMENSÕES USANDO NDIM UM VETOR COM VALORES 1,2,3,4 E VERIFIQUE SE A ÚLTIMA DIMENSÃO TEM O VALOR 4:

import numpy as np

arr = np.array([1,2,3,4], ndmin = 5)
print(arr)
print('Shape do array: ', arr.shape) 