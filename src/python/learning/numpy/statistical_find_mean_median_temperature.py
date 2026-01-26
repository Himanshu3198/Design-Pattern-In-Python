import numpy as np

temperature = np.array([95, 82, 67, 74, 58, 52])

mean = np.mean(temperature)
median = np.median(temperature)
max = np.max(temperature)
min = np.min(temperature)
above_average = temperature[temperature >mean]
standard_deviation = np.std(temperature)


summary = {"mean":mean,
           "median":median,
           "max_temp":max,
           "min_temp":min,
           "above_average":above_average,
           "standard_deviation":standard_deviation
           }

print(f"summary: {summary}")
