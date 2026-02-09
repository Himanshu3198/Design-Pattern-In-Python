import pandas as pd
# with help of multiIndex we can access a row by sets of values
arrays = [
    ["India", "India", "USA", "USA"],
    [2022, 2023, 2022, 2023]
]

index = pd.MultiIndex.from_arrays(arrays,names=("Country","Year"))
df = pd.DataFrame(
    {"Revenue":[500,200,1000,2000]},index=index)

print(df.head(2))

print("Access by",df.loc[("USA",2023)])

# Select all rows for a year (by level)
print("df.xs",df.xs("USA", level="Country"))

# filter by revenue
df[df["Revenue"] == 1000]