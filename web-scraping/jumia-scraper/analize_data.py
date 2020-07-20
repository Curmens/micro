import pandas as pd
import numpy as np


filename = 'printer_data.csv'

df = pd.read_csv(filename)
df.dropna(how='all')
# print(df[df['Product Name'] == 'NaN'])
df = df.drop(df[df['Product Name'] == df.isna(np.nan)].index)
print(df)
