import pandas as pd

dataset = {
    'carros':['BMW','VOLVO','FORD','HYUNDAI','VW'],
    'passageiro':[4,7,3,2,8]
    }

minhavar = pd.DataFrame(dataset)

print(minhavar)

print(pd.__version__)