import numpy as np

# generate factorial of 5
n = 5
arr = np.arange(1,n+1)
fact = np.prod(arr)
print(f"factorial of 5 is: {fact}")


# advanced version

nums =[3,4,5]

factorials = [np.prod(np.arange(1,x+1)) for x in nums]
print(f"factorials are: {factorials}")

# cummulative product

arr = np.arange(1, 6)
cum_factorial = np.cumprod(arr)
print(cum_factorial)