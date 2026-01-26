import numpy as np
# spread-how much scores vary within each subject
# from src.python.learning.numpy.statistical_find_mean_median_temperature import standard_deviation

# IQR (Interquartile Range) – robust spread

# IQR = difference between 75th percentile (Q3) and 25th percentile (Q1)

# find mean,standard_deviation,range(max-min),iqr



scores ={
    "Math":[23,56,78,97,10,30,80],
    "Physics":[25,46,78,64,85,30],
    "Chemistry":[35,45,78,76,23,11]
}

data = {}
for subject,marks in scores.items():
    arr = np.array(marks)
    data[subject] = {"mean:":np.mean(arr),
                      "standard_deviation: ":np.std(arr),
                     "range: ":np.max(arr)-np.min(arr),
                     "IQR(range between 25-75% ":np.percentile(arr,75)-np.percentile(arr,25)
    }

print("Analysis: ",data)