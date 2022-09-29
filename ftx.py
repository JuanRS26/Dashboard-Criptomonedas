import pandas as pd
import requests

markets = requests.get('https://ftx.com/api/markets').json()
df = pd.DataFrame(markets['result'])
# df.set_index('name', inplace = True)
# df2 = df.T

print(df.loc[163].to_string())