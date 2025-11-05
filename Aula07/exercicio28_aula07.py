import pandas as pd

a = [1,7,2]
var = pd.Series(a, index = ['x', 'y', 'z'])
print(var['x'])
