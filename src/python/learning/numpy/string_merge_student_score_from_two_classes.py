import numpy as np
# Merge Student Scores from Two Classes

class1 = {
    "names": ["Alice", "Bob", "Charlie"],
    "scores": [85, 90, 78]
}

class2 = {
    "names": ["David", "Eva", "Frank"],
    "scores": [88, 92, 80]
}

name1 = np.array(class1["names"])
name2 = np.array(class2["names"])

merge_name = np.concatenate((name1,name2))
score1 = np.array(class1["scores"])
score2 = np.array(class2["scores"])
merge_score = np.concatenate((score1,score2))

class3 = {
    "names":merge_name,
    "merge_score":merge_score
}

print(class3)