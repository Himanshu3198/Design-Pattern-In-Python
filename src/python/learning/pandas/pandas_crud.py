import pandas as pd

data = {
    "id" : [1,2,3,4,5,6,8,9,10],
    "name":["Amit","Rahul","Neha","Priya","rj","mahesh","Amit","Rajesh",None],
    "salary":[50000,60000,55000,30000,20000,80000,80000,100000,500000]
}

df = pd.DataFrame(data)
# print(df)

# random access
# print(df.sample(2))
print("accessing the particular record based on condition")
print(df.loc[df["name"] == "mahesh",:])

# // accessing the records in range of first 3 with name and id
print("accessing the records in range of first 3 with name and id")
print(df.iloc[0:3,0:2])

# accessing use column
print("accessing salary within first four row and salary >= 50000")
print(df.loc[(df.index <4) & (df["salary"] >= 50000),["salary"]])


# // searching with string
print("search with contains pr")
print(df.loc[df["name"].str.contains("Pr"),:])

print("Search ends with sh")
print(df.loc[df["name"].str.endswith("sh"),:])


# // isin in pandas
print("printing df wih ids in 3 to 5")
print(df[df["id"].isin([3,4,5])])

# not in in pandas
print("printing records not in")
print(df[~df["id"].isin([3,4,5])])

# sorting by multiple columns
print("sorting by columns in descending")
print(df.sort_values(by="salary",ascending=False))


# basic aggregation
print("print max salary")
print(df["salary"].max())

print("print mean salary")
print(df["salary"].mean())

print("print sum salary")
print(df["salary"].sum())

# groupby with aggregation
print("max salary with same name")
print(df.groupby("name")["salary"].max())

# adding new element
df["bonus"] = df["salary"]*0.1
print("after adding new column")
print(df.head(5))


# updating the name
print("update the name column with rj to rajesh")
df.loc[df["name"] == "rj",["name"]] ="Rajesh"
print(df)

# fillna with "kuch bhi"
df.fillna("kuch bhi",inplace=True)
# removing a element
print("after removing the name")
del df["name"]
print(df.head(5))
