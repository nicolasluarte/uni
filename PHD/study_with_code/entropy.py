import numpy as np
import matplotlib.pyplot as plt

# probability of observing a response with a spike-count rate 'r'

# create spike events

class neuron:
    def __init__(self, variance, threshold):
        self.variance = variance
        self.threshold = threshold

    def activity(self):
        return(np.random.normal(0, self.variance, 1))

    def spike(self):
        activity = self.activity()
        if activity >= self.threshold:
            return(1)
        else:
            return(0)

    def simulate(self, n):
        simulation_run = [self.spike() for f in range(n)]
        return(simulation_run)


def plot_spikes(data):
    x = list(range(0, len(data)))
    y = data
    plt.step(x, y, color="black")
    plt.axis('off')
    plt.show()
