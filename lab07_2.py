# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 04:27:30 2021

@author: Adri Saha
"""
#Name: Adri Saha
#ID: 2019-1-60-024

#Task 2

import pandas as pd
import matplotlib.pyplot as plt
import lab07_my_module as task2

df = pd.read_csv('SimpleLinearRegression.csv')
'''df.colums = ['No', 'X1 transaction', 'X2 house age', 
             'X3 distance to the nearest MRT station',	
             'X4 number of convenience stores','X5 latitude',
             'X6 longitude','Y house price of unit area']'''

#%%
#splitting data
x = df['YearsExperience']
y = df['Salary']
print(df.head(5))
x_train, y_train, x_test, y_test = task2.train_test_split_Adri(x, y, 1/3)

#%%
#subplot 1 for train set

plt.figure(figsize=(10,4),dpi=100)
plt.subplot(1,2,1)
ax = plt.gca()
ax.set_facecolor('#c1c6fc')
y_pred = task2.y_pred_Adri(x_train, y_train)
plt.scatter(x_train, y_train, s=8)
plt.plot(x_train, y_pred, color = 'red')
plt.xlabel("YearsExperience", size=20, color='#4b0101')
plt.ylabel("Salary", size=20, color='#4b0101')
plt.title("Training Set", size=20, color='#4b0101')
#%%
#subplot 2 for test set

#plt.figure(figsize=(10,4),dpi=100)
plt.subplot(1,2,2)
ax2 = plt.gca()
ax2.set_facecolor('#95d0fc')
y_pred = task2.y_pred_Adri(x_test, y_test)
plt.scatter(x_test, y_test, s=8, color='purple')
plt.plot(x_test, y_pred, color='red')
plt.xlabel("YearsExperience", size=20, color='#750851')
plt.ylabel("Salary", size=20, color='#750851')
plt.title("Test Set", size=20, color='#750851')
plt.show()

#%%
y_pred = task2.y_pred_Adri(x_test, y_test)
print('R-squared value: ',task2.r_squared_Adri(y_test, y_pred))
print('MSE value: ',task2.mse_Adri(y_test, y_pred))
print('MAE value: ',task2.mae_Adri(y_test, y_pred))