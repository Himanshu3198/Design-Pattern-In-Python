import numpy as np
from numpy import random as rand
songs = np.array(["songA","songB","songC","songD","songE"])

idx = np.array([0,3,4])
playlist = songs[idx]
print(f"playlist: {playlist}")

# generate random playlist

rand_idx =  rand.randint(0,len(songs),size=4)
print(f"random playlist: {songs[rand_idx]}")