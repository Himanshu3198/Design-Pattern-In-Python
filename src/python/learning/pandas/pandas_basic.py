import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}


df = pd.DataFrame(mydataset)

row,col = df.shape
print(f"row is{row} and col is{col}")


# series in pandas is like column in table that can hold data of any type and its 1d array

a = [1,2,3]
print("===series demo===")
srs = pd.Series(a)
print(srs[0])

# label : if index is not specified  then it creates 0 to size index . and we can create custom index


a_idx = pd.Series(a,index=["x","y","z"])
print(a_idx)

# Create a simple Pandas Series from a dictionary:
calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)

