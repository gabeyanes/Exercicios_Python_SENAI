#EXERCICIO01 AULA03 IF ELSE

# FAÇA UM PROGRAMA QUE LEIA 2 NOTAS DE UM ALUNO, CALCULE A MÉDIA E IMPRIMA APROVADO OU REPROVADO(PARA SER APROVADO A MÉDIA DEVE SER NO MÍNIMO 6)

nota1 = float(input('Insira a nota da prova A1: '))
nota2 = float(input('Insira a nota da prova A2: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f'Parabéns você passou com uma média de {media}')
else:
    print(f'Sua média foi insuficiente para passar, aqui sua média {media} ')

    

