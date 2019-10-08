"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

from compute_sta import compute_sta

# importing package to opening pickle file
import pickle

FILENAME = 'c1p8.pickle'

# opening pickle file
with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']


# Fill in these values
time_window = 300
sampling_period = 1000*(1/500) # in ms - the sampling rate was 500 Hz
num_timesteps = int(time_window/sampling_period) # if response window to check is 300 ms, and the sampling period is 2 ms, then number of steps in the window is 150

sta = compute_sta(stim, rho, num_timesteps) # spike triggered average vector

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period # time plot

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()
