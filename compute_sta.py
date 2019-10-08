"""
Created on Wed Apr 22 15:21:11 2015

Code to compute spike-triggered average.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


# calculating the spike triggered average is an example of a feature to use

def compute_sta(stim, rho, num_timesteps):
    """Compute the spike-triggered average from a stimulus and spike-train.
    
    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA
        
    Returns:
        spike-triggered average for num_timesteps timesteps before spike"""
    
    # rho is the vector showing if there was a spike (1) or not (0)
    
    sta = np.zeros((num_timesteps,)) # check what happens without the comma

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps # this is array of spike times, need to understand this more

    # Fill in this value. Note that you should not count spikes that occur
    # before 300 ms into the recording.

    num_spikes = len(spike_times) # outputs the number of spikes
    print(num_spikes)
    

    # Compute the spike-triggered average of the spikes found.
    # To do this, compute the average of all of the vectors
    # starting 300 ms (exclusive) before a spike and ending at the time of
    # the event (inclusive). Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.
    # 
    # Your code goes here:
    
    for i in spike_times:
        sta = sta + stim[i-num_timesteps:i]
    
    sta = sta/num_spikes
    
    return sta