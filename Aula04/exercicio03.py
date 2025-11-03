# EXERCICIO03 AULA04

# FAÇA UM PROGRAMA EM PYTHON QUE RECEBE A TEMPERATURZA DE Z CLIENTES E IMPRIMA A MENSAGEM DE SE A TEMPERATURA ESTA NORMAL (MENOR QUE 37,2C)
# OU ESTÁ EM ESTADO FEBRIL(37,3C A 38C) OU COM FEBRE(38,1 A 39C) E COM FEBRE ALTA(ACIMA 39.1). NO FINAL MOSTRE A QUANTIDADE DE PESSOAS ANALISADAS
# E A MÉDIA DE TEMPERATURA

print('--BEM VINDO AO HOSPITAL PYTHON--')

media = 0
soma = 0
qntd_pacientes = int(input('Me informa a quantidade de pacientes: '))

for i in range(qntd_pacientes):
    paciente =  float(input(f'Qual a sua temperatura paciente número {i+1}:'))
    
    if paciente < 37.2:
        soma += paciente
        print(f'Sua temperatura está normal paciente {i+1}!')
    elif paciente >= 37.3 and paciente <= 38:
        soma += paciente
        print(f'Sua temperatura está febril paciente {i+1}!')
    elif paciente >= 38.1 and paciente <= 39:
        soma +=paciente
        print(f'Sua temperatura está de febre paciente {i+1}!')
    elif paciente >= 39.1:
        soma += paciente
        print(f'Sua temperatura está de febre altissima paciente {i+1}!')
        
    
print(f'\n Foi o total de {qntd_pacientes} atendidos e a média de temperatura é {soma/qntd_pacientes:.2f}!')
    
    
    
    