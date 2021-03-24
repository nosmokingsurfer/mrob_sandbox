import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import mrob

import uncertainty
from  uncertainty import sigma_visualize_3d

import plotly.express as px

plt.figure(figsize=(10,10))
plt.suptitle('Covariance ellipsoid visualisation v.s. \ncorresponding Monte Carlo direct sampling distribution')
# sigma = np.diag([.3,.01,0.01,0.01,0.01,0.02])
mean = np.array([0,0,0,0,0,0])

T = mrob.geometry.SE3([0,0,0,1,0,0])
sigma = np.diag([0.01,0.01,0.1,0.001,0.001,0.001])

axes, circumferences = sigma_visualize_3d(T,sigma)

df = pd.DataFrame(columns = ['x','y','z'])

for key,val in axes.items():
    tmp = pd.DataFrame(val,columns=['x','y','z'])
    tmp['label'] = key
    df = pd.concat([df,tmp])

for key,val in circumferences.items():
    tmp = pd.DataFrame(val,columns=['x','y','z'])
    tmp['label'] = key
    df = pd.concat([df,tmp])


fig = px.line_3d(data_frame=df,x='x',y='y',z='z',color='label',hover_name='label')
fig.update_layout(scene = dict(
        xaxis = dict(nticks=4, range=[0.5,1.5],),
                     yaxis = dict(nticks=4, range=[-0.5,0.5],),
                     zaxis = dict(nticks=4, range=[-0.5,0.5],),))
fig.show()