import pandas as pd

df = pd.DataFrame({"age":[1,5,6,12,3,6,8,10],
                   "name":["a","b","c","d","e","f","g","i"]})


print(df.sort_values("age",ascending=False))