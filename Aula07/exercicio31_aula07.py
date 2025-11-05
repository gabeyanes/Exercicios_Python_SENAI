import pandas as pd

data = {
    'calorias' : [460,390,370,350,380],
    'duracao' : [50,40,30,25,42]
}

var = pd.DataFrame(data)

print(f'O dado está localizado aqui:\n{var.loc[[0,3]]}')

print(var)
