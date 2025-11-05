import pandas as pd

data = {
    'calorias' : [460,390,370,350,380],
    'duracao' : [50,40,30,25,42]
}

var = pd.DataFrame(data, index=['1', '2', '3','4','5'])

print(var.loc['1'])

