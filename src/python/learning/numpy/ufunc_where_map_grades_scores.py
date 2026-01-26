import numpy as np

# map the scores with grades  using where
scores = np.array([95, 82, 67, 74, 58, 52])

grades = np.where(scores >=90,'A',
                  np.where(scores >=80,'B',
                   np.where(scores>=70,'C',
                   np.where(scores >= 60,'D','E'))))

print(f"grades are: {grades}")