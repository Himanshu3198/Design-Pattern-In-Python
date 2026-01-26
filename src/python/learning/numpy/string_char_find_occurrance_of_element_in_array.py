# Find occurrences of a substring in a NumPy array
import numpy as np

fruits = np.array(["apple","banana","apple","apple","mango","pomegrante"])

find_apple = np.char.count(fruits,"apple")
print(find_apple)
count_apple = np.sum(find_apple)
print(count_apple)