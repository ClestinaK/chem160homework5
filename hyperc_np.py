import math, time
import numpy as np

ntrials = 1000000
dist = 0
start_time = time.process_time()

for i in range(ntrials):
    x1 = np.random.random(ntrials)
    y1 = np.random.random(ntrials)
    z1 = np.random.random(ntrials)
    x2 = np.random.random(ntrials)
    y2 = np.random.random(ntrials)
    z2 = np.random.random(ntrials)
    dist = np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

e_time = time.process_time() - start_time
print("Ave dist = %9.7f  Elapsed time = %6.2f"%(dist, e_time))