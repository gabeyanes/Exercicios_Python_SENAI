# EXERCICIO04 AULA03

# CRIE UM PROGRAMA PARA ENTRAR COM A BASE A ALTURA DE UM RETÂNGULO E IMPRIMIR RESPECTIVAMENTE O PERÍMETRO E A ÁREA CORRESPONDENTE

base = float(input('insira o valor da base do retângulo: '))
altura = float(input('insira o valor da altura do retângulo: '))

area = base * altura
perimetro = (base * 2) + (altura * 2)

print(input(f'aqui está a área do retângulo {area} e aqui está o perimetro {perimetro}'))