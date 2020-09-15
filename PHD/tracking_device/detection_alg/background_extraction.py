%matplotlib qt
import time
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from scipy.stats import norm, gaussian_kde
from sklearn.neighbors import KernelDensity
import statsmodels.api as sm
from fastkde.fastKDE import pdf
from fastkde import fastKDE

img = cv2.imread('background.png', 0)
c_img = cv2.imread('rat_background.png', 0)
flatten_img = img.flatten()
flatten_c_img = c_img.flatten()
hist = plt.hist(flatten_img, bins=30, density=True)
plt.show()

kde = gaussian_kde(flatten_img)
u = np.linspace(200, 255, 1000)
v = kde.evaluate(u)
plt.plot(u, v, 'k')
plt.show()

plt.imshow(c_img)
plt.show()

xx = 0
for x in range(0, 365):
    for y in range(0, 640):
        print(kde.evaluate(c_img[x, y]))
        print(xx)
        xx += 1

x = np.linspace(200, 255, 233600)[:, np.newaxis]
flatten_img.shape = (img.size, 1)
kde = KernelDensity(bandwidth=1.0, kernel = 'gaussian').fit(flatten_img)
kd_vals = np.exp(kde.score_samples(x))

dens = sm.nonparametric.KDEUnivariate(img.flatten())
dens.fit()
kde = gaussian_kde(img.flatten())


start = time.time()
dens.evaluate(c_img.flatten()[0:1000])
end = time.time()
print(end - start)




