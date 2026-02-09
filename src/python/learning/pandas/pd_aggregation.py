import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])

print(s.sum())     # 150
print(s.mean())    # 30.0
print(s.min())     # 10
print(s.max())     # 50
print(s.count())   # 5


df = pd.DataFrame({"City":["NY","DL","KA"],
                    "Revenue":[4000,2000,6000],
                    "Employee":[50,20,30]})

print(f"sum={df.sum()}")
# print(f"count={df.count(axis=1)}")
# print(f"max={df.max(axis=1)}")
# print(f"mean={df.mean(axis=1)}")