import numpy as np


arr = np.array([1,2,3,4,6,7,2,12,32])

odd = arr[arr%2 == 1]
print(f"odd: {odd}")