import pandas as pd

# combine two dataframe based on common key using merge and concat


data1 = {"id":[1,2,3],
         "name":["akask","rake","mukes"]}

data2 = {"id":[1,2,4],
         "is_married":["YES","NO","YES"]
         }

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)


data3 = pd.merge(df1,df2,on="id",how="inner")
print("data3 using merge",data3)

data4 = pd.concat([df1,df2],axis=1)
print("data4 using concat",data4)