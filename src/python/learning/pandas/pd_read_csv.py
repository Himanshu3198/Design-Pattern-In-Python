import pandas as pd


df = pd.read_csv('data.csv')
print(df)
row,col = df.shape
print(f"row={row},col={col}")