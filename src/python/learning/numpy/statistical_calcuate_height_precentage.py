import numpy as np

heights = [150, 155, 160, 165, 170, 175, 180]

summary = {
    "bottom 25% =":np.percentile(heights,25),
    "bottom 50%= ":np.percentile(heights,50),
    "top 25% =":np.percentile(heights,75)
}

print(summary)