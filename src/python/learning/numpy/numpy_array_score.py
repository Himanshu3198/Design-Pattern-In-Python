import numpy as np
# print the array , average,min,max
scores = [78, 85, 90, 88, 76]

arr = np.array(scores)

print(arr)

# sort the arr
arr.sort()

# find average or mean

print(f"average is : {arr.mean()}")

# find the max and min value
print(f"max,min{arr.max()},{arr.min()}")

