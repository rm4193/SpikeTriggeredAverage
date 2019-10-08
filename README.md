# SpikeTriggeredAverage
Calculating spike triggered average of the H1 motion-sensitive neuron using the dataset obtained from Dr Robert de Ruyter van Steveninck


This project calculates the spike-triggered average, using a window of 300 ms before the H1 neuron spikes. The window is applied to the stimulus array in the pickle file. The goal is to average all of the 300 ms stimulus windows before a spike occurs, to see what is the common stimulus feature that causes the neuron to fire.

compute_sta.py file has a function to compute the spike-triggered average

main.py file allows for you to change the variables in the compute_sta function from compute_sta.py file
