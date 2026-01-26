import numpy as np
#  print every element third element from right
arr = np.array([12,23,41,42,4,3,4,6,123,34,89,98,76,53])

ans = arr[-3::-3]
print(f"every third element is={ans}")

reverse = arr[::-1]
print(f"reverse of arr: {reverse}")

# filter even and greater than 50
filter = arr[ (arr%2 ==0) & (arr>50)]

print(f"filter above 50 and even: {filter}")