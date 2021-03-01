import matplotlib.pyplot as plt
import numpy as np

import mrob

import uncertainty
from  uncertainty import sigma_visualize, compound_2nd



# defining two poses with uncertainty to compound
xi_1 = np.array([0,0,0,0.5,0,0])
T_1 = mrob.geometry.SE3(xi_1)
sigma_1 = np.diag([0,0,0.01,0.01,0.01,0])

xi_2 = np.array([0,0,1.5,1.0,0,0])
T_2 = mrob.geometry.SE3(xi_2)
sigma_2 = np.diag([0,0,0.1,0.01,0.01,0])

# performing 2nd order compounding of two poses
T,sigma = compound_2nd(T_1, sigma_1, T_2, sigma_2)


plt.figure(figsize=(10,10))
plt.title('Second order pose compounding')
sigma_visualize(T_1, sigma_1, label='sigma_1',color='r')
sigma_visualize(T_2, sigma_2, label='sigma_2',color='g')
sigma_visualize(T,sigma, label='2nd order \ncompound',color='b')


sigma_visualize(T,sigma, label='2nd order \ncompound',color='yellow')


plt.grid()
plt.axis('equal')
plt.show()
