def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    data3 = pd.merge(employee,bonus,on="empId",how="left")
    mask = (data3["bonus"].isna()) | (data3["bonus"] < 1000)
    return data3.loc[mask,["name","bonus"]]

def second_highest_salary(emp: pd.DataFrame) -> pd.DataFrame:
    rec = emp["salary"].drop_duplicates().sort_values(ascending=False)
    if len(rec) < 2:
        return pd.DataFrame({"SecondHighestSalary":[None]})
    return  pd.DataFrame({"SecondHighestSalary":[rec.iloc[1]]})

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person[person.duplicated("email")]
    return df[["email"]].drop_duplicates().rename(columns={"email":"Email"})


import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    filtered = customers[~customers["id"].isin(orders["customerId"])]
    filtered_name = filtered[["name"]]
    return filtered_name.rename(columns={"name":"Customers"})