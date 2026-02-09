import pandas as pd
from pandas.io.formats.info import series_sub_kwargs

"""map works on series_sub_kwargs
applymap works on dataframes
apply works on both"""


s = pd.Series([1,3,2,5,10],index=["a","b","c","d","e"])
square = s.map(lambda x:x*x)
print(square)


# with dictionary

sex  = pd.Series(["m","f","m"])
sex_map = sex.map({"m":"Male","f":"Female"})
print(sex_map)

