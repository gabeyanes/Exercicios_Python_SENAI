import pandas as pd

df = pd.read_json('C:\Temp\data.json')

print(pd.options.display.max_rows)
print(df.to_string())