import pandas as pd

# Task
#
# Select employees from the "IT" department whose salary is greater than 60,000
#
# Display only id, name, and salary
#
# Sort the result by salary in descending order
#
# Update the salary by +10% for employees whose name is "Rahul"
data = {
    "id": [101, 102, 103, 104, 105, 106],
    "name": ["Rahul", "Amit", "Neha", "Rahul", "Priya", "Karan"],
    "dept": ["IT", "HR", "IT", "Finance", "IT", "HR"],
    "salary": [65000, 50000, 72000, 80000, 60000, 55000]
}

df = pd.DataFrame(data)

# print(df)

# Step 1: Filter
mask = (df["dept"] == "IT") & (df["salary"] > 60000)

# Step 2: Select required columns
filtered = df.loc[mask, ["id", "name", "salary"]]

# Step 3: Sort descending
result = filtered.sort_values(by="salary", ascending=False)

print(result)

# Step 4: Update Rahul salary by 10%
df.loc[df["name"] == "Rahul", "salary"] *= 1.1


# =======================================================

# Find the top 2 highest-paid employees.
print("Find the top 2 highest-paid employees.")
sort = df.sort_values(by="salary",ascending=False)
print(sort.iloc[0:2,[1,3]])
print("Count how many employees are in each department.")
count = df.groupby("dept")["id"].count()
print(count)

print("Find employees whose name starts with R.")
name_mask = df["name"].str.startswith("R")
print(df.loc[name_mask,:])


print("Find the average salary per department.")
print(df.groupby("dept")["salary"].mean())
print("max salary per department")
print(df.groupby("dept")["salary"].max())
print("min salary per department")
print(df.groupby("dept")["salary"].min())

print("Increase salary by 5% for employees earning less than 60,000.")
df.loc[df["salary"] < 60000,"salary"] *=(5/100)
print(df)

