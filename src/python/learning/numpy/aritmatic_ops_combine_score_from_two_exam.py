import numpy as np
from numpy.ma.extras import average

exam1 = np.array([13,23,42,26,36,37,33])
exam2 = np.array([23,22,12,30,56,67,77])

# sum of both exams
sum_arr = exam1+exam2
print(f"sum_arr: {sum_arr}")

# average of both exam

avg_arr =(exam1+exam2)/2
print(f"avg of both exam: {avg_arr}")

# max of both exam

max_arr = np.maximum(exam1,exam2)
print(f"max of both: {max_arr}")