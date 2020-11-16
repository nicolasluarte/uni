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
# high variability
h_reward = np.random.normal(100, 1, 100)
# low variability
l_reward = np.random.normal(100, 10, 100)

for i in range(10):
    error, estimate = update(true_reward[i], estimates[-1], 0.9)
    estimates.append(estimate)
    errors.append(error)
    print(error)

estimates_h = [0]
errors_h = []
for i in range(100):
    error_h, estimate_h = update(h_reward[i], estimates_h[-1], 0.9)
    estimates_h.append(estimate_h)
    errors_h.append(error_h)
    print(error_h)

estimates_l = [0]
errors_l = []
for i in range(100):
    error_l, estimate_l = update(l_reward[i], estimates_l[-1], 0.9)
    estimates_l.append(estimate_l)
    errors_l.append(error_l)
    print(error_l)


smoothed_errors = gaussian_filter1d(errors, sigma=2)
smoothed_errors_h = gaussian_filter1d(errors_h, sigma=2)
smoothed_errors_l = gaussian_filter1d(errors_l, sigma=2)


unsign_h = [abs(ele) for ele in errors_h]
unsign_l = [abs(ele) for ele in errors_l]
h = pd.Series(unsign_h).cumsum()
l = pd.Series(unsign_l).cumsum()
h = pd.Series(unsign_h)
l = pd.Series(unsign_l)
x = list(range(0, 100))

fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)
ax.plot(x, h, color='black')
ax.plot(x, l, color='gray')
ax.xaxis.set_tick_params(which='major', size=4, width=1, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=4, width=1, direction='in', right='on')
ax.set_xlabel('Trial number', labelpad=10)
ax.set_ylabel('Reward prediction error cumulative sum', labelpad=10)
custom_lines = [Line2D([0], [0], color='gray', lw=4),
                Line2D([0], [0], color='black', lw=4)]
ax.legend(custom_lines, [r'$N \sim (100, 10)$', r'$N \sim (100, 1)$'])
plt.savefig('figure4.png', dpi=300, transparent=False, bbox_inches='tight')

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



def graph(func, x_range):
   x = np.arange(*x_range)
   y = func(x)
   plt.plot(x, y)

graph(lambda x: 100*(np.power(0.8, x)), (0,100))


x = np.linspace(1, 100, 100)
y1 = np.exp(-x/20)
y2 = np.exp(-x/5)
fig = plt.figure(figsize=(3,3))
ax = fig.add_subplot(111)
ax.plot(x, y1, color='black')
ax.plot(x, y2, color='gray')
ax.xaxis.set_tick_params(which='major', size=4, width=1, direction='in', top='on')
ax.yaxis.set_tick_params(which='major', size=4, width=1, direction='in', right='on')
ax.set_xlabel('Time', labelpad=10)
ax.set_ylabel('Value', labelpad=10)
custom_lines = [Line2D([0], [0], color='gray', lw=4),
                Line2D([0], [0], color='black', lw=4)]
ax.legend(custom_lines, ['Immediate reward bias', 'Normal'])
plt.show()
