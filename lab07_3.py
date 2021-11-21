# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 04:27:43 2021

@author: Adri Saha
"""
#Name: Adri Saha
#ID: 2019-1-60-024

#Task 3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import lab07_my_module as task3

df = pd.read_csv('RealEstate.csv')
'''df.colums = ['No', 'X1 transaction', 'X2 house age', 
             'X3 distance to the nearest MRT station',	
             'X4 number of convenience stores','X5 latitude',
             'X6 longitude','Y house price of unit area']'''

#%%
df['bias']=1
print(df.head(5))
#%%
x = df[['bias', 'X2 house age', 'X6 longitude']]
y = df[['Y house price of unit area']]

#%%
x = np.array(x)
y = np.array(y)

#%%
w=task3.weights_2019_1_60_24(x,y)
y_pred =w[0]+w[1]*df['X2 house age']+w[2]*df["X6 longitude"]

#%%
fig = plt.figure()
fig,ax=plt.subplots(subplot_kw={"projection": "3d"})
ax = plt.gca()
ax.set_facecolor('#c1c6fc')
surf= ax.scatter(x[:,0],x[:,1],y,cmap=cm.coolwarm,linewidth=0, color= 'purple',antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')
plt.title("Multiple Linear Regression")
plt.show()

#%%
print('R-squared value: ', task3.r_squared_Adri(y, y_pred))
print('MSE value: ', task3.mse_Adri(y, y_pred))
print('MAE value: ', task3.mae_Adri(y, y_pred))