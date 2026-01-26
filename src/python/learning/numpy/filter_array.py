import numpy as np

# generate odd number from 4 to 9
arr =  np.arange(4,10)
arr_filter = arr[arr%2 != 0]
print(f"odd elements are={arr_filter}")

# second approch

filt = []

for x in arr:
      filt.append(x%2 == 1)

ans = arr[filt]



