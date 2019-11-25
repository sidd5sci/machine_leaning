



from genrateData import *
import pandas as pd
import numpy as np
from scipy.special import expit

import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib inline


import seaborn as sns
import plotly
import plotly.graph_objs as go

plotly.offline.init_notebook_mode(connected=True)


### Input layer


x1,x2,label = getTraingData()
df = pd.DataFrame({'x1':x1,'x2':x2,'label':label})
# ploting the input data
sns.lmplot(x= 'x1',y='x2',hue = 'label',data= df,fit_reg=False)


### Hiden layer 


# neuron 1 of hidden layer 
b1 = 0 # bias 
w1 = [-0.4, 0.6] # weights
z1 = w1[0] * x1 + w1[1]*x2 +b1  # Sums of multiplications of weights and biases 
a1 = expit(z1) # activation function 

# neuron 2 of hidden layer 
b2 = 0 # bias 
w2 = [0.2, 0.8] # weights
z2 = np.dot(w2,[x1,x2]) +b2  # Sums of multiplications of weights and biases 
a2 = expit(z2) # activation function 

# neuron 3 of hidden layer 
b3 = 0 # bias 
w3 = [0.7, 0.8] # weights
z3 = np.dot(w3,[x1,x2]) +b3  # Sums of multiplications of weights and biases 
a3 = expit(z3) # activation function 



### output layer

# output neuron 1
b_out = 0
w_out = [-1.2,2.0,0.1]
z_out = np.dot(w_out,[a1,a2,a3]) = b_out
a_out = expit(z_out)
# https://erp.netcracker.com/ncobject.jsp?id=9154858648913969199

