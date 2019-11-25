



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

x1,x2,label = getTraingData()

df = pd.DataFrame({'x1':x1,'x2':x2,'label':label})

