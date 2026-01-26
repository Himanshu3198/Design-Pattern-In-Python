import numpy as np
from numpy import random as rand
  # random dice simulation - create random number arr of size n
n = 3

arr = []

for i in range(0,3):
    x = rand.randint(6)
    arr.append(x)

print(f"arr is ={arr}")


# generate random array using randint

ar = rand.randint(100,size=5)
print(f"ar={ar}")