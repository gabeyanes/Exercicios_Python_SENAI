# EXERCICIO05 AULA03

# CRIE UM PROGRAMA QUE DADOS O VALOR, A TAXA E O TEMPO, EFETUAR O CÁLCULO DO VALOR DE UMA PRESTAÇÃO EM ATRASO, UTILIZANDO A FÓRMULA: "prestação = valor + (valor * (taxa/100) * tempo)"

valor = float(input('Valor do empréstimo: '))
tempo = int(input('Quantidade de parcelas(mês): '))
taxa = float(input('Taxa da prestação: '))

# taxa = taxa/100

prestacao = valor + (valor * (taxa/100) * tempo)

print(f'A sua prestação é {prestacao}.')