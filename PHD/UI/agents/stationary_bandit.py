import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random


class bandit_arm:
    def __init__(self, mean, variance):
        self.mean = mean
        self.variance = variance
        self.reward_history = []

    # Return reward
    def reward(self):
        r = np.random.normal(self.mean, self.variance)
        self.reward_history.append(r)
        return r


class agent:
    actions = [0, 1]

    def __init__(self, alpha, n_trials=1):
        self.alpha = alpha
        self.estimate = [(0, 'null')]
        self.actions = []
        self.n_trials = n_trials

    def estimate_value(self, reward, arm):
        filtered = [t for t in self.estimate if t[1] == arm]
        if len(filtered) == 0:
            filtered = self.estimate
        self.estimate.append((filtered[-1][0] + ((1/self.n_trials) * (reward - filtered[-1][0])), arm))
        print(self.estimate)

    def act(self):
        action_taken = random.choice(agent.actions)
        self.actions.append(action_taken)
        self.n_trials = self.n_trials + 1
        return action_taken




a = bandit_arm(100, 5)
b = bandit_arm(50, 5)

banana = agent(0.9)

for i in range(1000):
    action = banana.act()
    if action == 0:
        a.reward()
        banana.estimate_value(a.reward_history[-1], action)
    else:
        b.reward()
        banana.estimate_value(b.reward_history[-1], action)
