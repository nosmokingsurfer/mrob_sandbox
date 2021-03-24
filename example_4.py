import matplotlib.pyplot as plt
import numpy as np

import mrob

import uncertainty
from uncertainty import sigma_visualize, get_mc

plt.figure(figsize=(10,10))
plt.suptitle('Covariance ellipsoid visualisation')
sigma = np.diag([0,0,0.1,0.001,0.01,0])
mean = np.array([0,0,0,0,0,0])
sigma_visualize(mrob.geometry.SE3([0,0,0,1,0,0]), sigma=sigma,N = 100, K=[3], color='red')

plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])
plt.grid()
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.show()