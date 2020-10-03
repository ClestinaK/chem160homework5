import math, time, random
import numpy as np

ntrials = 100
dist = 0
start_time = time.process_time()

for i in range(ntrials):
    x1 = np.random.random(ntrials)
    y1 = np.random.random(ntrials)
    z1 = np.random.random(ntrials)
    x2 = np.random.random(ntrials)
    y2 = np.random.random(ntrials)
    z2 = np.random.random(ntrials)
    dist = np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))

e_time = time.process_time() - start_time
calc_dist = 1/105*(4+17*np.sqrt(2)-6*np.sqrt(3)+
            21*np.log(1+np.sqrt(2))+42*np.log(2+np.sqrt(3))-7*np.pi)
print("NTrials = ", ntrials)
print("Average Distance = ", dist)
print("Elapsed time = ", e_time)
print("Calculated Distance= ", calc_dist)
