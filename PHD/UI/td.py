import numpy as np
import pandas as pd
from scipy.ndimage.filters import gaussian_filter1d
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt


def update(reward, estimate, alpha):
    error = reward - estimate
    estimate = estimate + (alpha * error)
    return error, estimate


estimates = [0]
errors = []
true_reward = [100, 100, 100, 100, 100, 50, 50, 50, 50, 50]

for i in range(10):
    error, estimate = update(true_reward[i], estimates[-1], 0.9)
    estimates.append(estimate)
    errors.append(error)
    print(error)

smoothed_errors = gaussian_filter1d(errors, sigma=2)

fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)
ax.plot(errors, color='black')
ax.axvline(x=4, linestyle='--', color='gray')
ax.xaxis.set_tick_params(which='major', size=4, width=1, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=4, width=1, direction='in', right='on')
ax.set_xlabel('Trial number', labelpad=10)
ax.set_ylabel('Reward prediction error', labelpad=10)
plt.savefig('figure1.png', dpi=300, transparent=False, bbox_inches='tight')


estimates2 = [0]
errors2 = []

for i in range(1000):
    error2, estimate2 = update(np.random.normal(100, 1), estimates2[-1], 0.9)
    estimates2.append(estimate2)
    errors2.append(error2)
    print(error2)

estimates3 = [0]
errors3 = []

for i in range(1000):
    error3, estimate3 = update(np.random.normal(100, 10), estimates2[-1], 0.9)
    estimates3.append(estimate3)
    errors3.append(error3)
    print(error3)


s1 = pd.Series(errors2)
s2 = pd.Series(errors3)
x = list(range(0, 1000))

fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)
ax.plot(x, s1.rolling(100).std(), color='black')
ax.plot(x, s2.rolling(100).std(), color='gray')
ax.xaxis.set_tick_params(which='major', size=4, width=1, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=4, width=1, direction='in', right='on')
ax.set_xlabel('Trial number', labelpad=10)
ax.set_ylabel('Reward prediction error standard deviation', labelpad=10)
custom_lines = [Line2D([0], [0], color='gray', lw=4),
                Line2D([0], [0], color='black', lw=4)]
ax.legend(custom_lines, [r'$N \sim (100, 10)$', r'$N \sim (100, 1)$'])
plt.savefig('figure2.png', dpi=300, transparent=False, bbox_inches='tight')
