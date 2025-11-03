# EXERCICIO01 AULA04

# CONSTRUA UM PROGRAMA EM PYTHON UTILIZANDO OS COMANDOS APRENDIDOS ATÉ AGORA PARA ENCONTRAR TODOS OS NÚMEROS PARES ENTRE 1 E 100.

for i in range(1,101,1):
    if i % 2 == 0:
        print(f'Esse numero é par {i}')
    else:
        print(f'Esse numero é impar {i}')