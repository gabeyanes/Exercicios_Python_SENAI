# EXERCICIO02 AULA03 IF ELSE

# FAÇA UM PROGRAMA QUE PEÇA DOIS NÚMEROS AO USUÁRIO E MOSTRE QUAL É O MAIOR E QUAL O MENOR

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

if num1 > num2:
    print(f'O primeiro número {num1} é maior que o segundo número {num2}')
elif num1 < num2:
    print(f'O segundo número {num2} é maior que o primeiro número {num1}')
elif num1 == num2:
    print(f'Ambos os números são iguais.')
else:
    print(f'Algum dado foi inserido de forma errada')
