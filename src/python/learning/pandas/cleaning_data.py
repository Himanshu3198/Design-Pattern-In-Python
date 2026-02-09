import pandas as pd

df = pd.read_csv('data.csv',sep ='|')
print(df)
# drop the column with null values
new_df = df.dropna()
print(new_df)
# replace null with values
df2 = df.fillna({"name": "himanshu", "scores": 100})
print("==df2===")
print(df2)

# remove the duplicates from df

df3 = df.drop_duplicates()
print("===df3===")
print(df3)
