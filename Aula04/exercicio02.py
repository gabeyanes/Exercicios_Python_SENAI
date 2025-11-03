# EXERCICIO02 AULA04

# FAÇA UM PROGRAMA EM PYTHON (UTILIZE A ESTRUTURA FOR) QUE LEIA 10 VALORES INTEIROS E: 1° ENCONTRE E MOSTRE O MAIOR VALOR, 2° ENCONTRE E MOSTRE O MENOR VALOR & 3° CALCULE E MOSTRE A MÉDIA DOS NÚMEROS LIDOS.

soma = 0
media = 0
maior = float('-inf')
menor = float('inf')

for i in range(10):
    num = int(input(f'Insira {i+1}° valor:'))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
    
    soma += num
        
media = soma/10
print(f'o maior número é {maior} e o menor é {menor} e a média é {media}')
