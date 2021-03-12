import math
import matplotlib.pyplot as plt


def repetitions(rir, reps):
    exertion = list()
    i = 1
    for r1, r2 in zip(rir, reps):
        result = math.exp(-0.215 * (r1 + (r2 - i)))
        exertion.append(result)
        i += 1
    return exertion


rir = [3, 3, 3.5, 3, 4]
reps = [8, 6, 5, 5, 4]

result = repetitions(rir, reps)

print(result)

plt.plot(result)
plt.show()
