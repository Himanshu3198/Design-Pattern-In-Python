def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    data3 = pd.merge(employee,bonus,on="empId",how="left")
    mask = (data3["bonus"].isna()) | (data3["bonus"] < 1000)
    return data3.loc[mask,["name","bonus"]]