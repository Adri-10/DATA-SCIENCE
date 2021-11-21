# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:27:44 2021

@author: Adri Saha
"""

import pandas as pd

#%% problem 1
#Adri Saha
#2019-1-60-024

tf = pd.read_csv('iris.csv')
print(type(tf))
print(tf)
tf.columns = ['sepal.length','sepal.width','petal.length','petal.width','variety']
petal_length = tf[['petal.length']]
print(type(petal_length))

print("Mean: " ,petal_length.mean())
print("Standard Deviation: ",petal_length.std())
print("Variance: ",petal_length.var())
print("Lower Quartile: " ,petal_length.quantile(0.25))
print("Median: ",petal_length.quantile(0.5))
print("Median: " ,petal_length.median())
print("Upper Quartile: " ,petal_length.quantile(0.75))
print("Skewness: " ,petal_length.skew())
print("Kurtosis: " ,petal_length.kurt())
print("Min: ",petal_length.min())
print("Max: ",petal_length.max())
#%% problem 2
#Adri Saha
#2019-1-60-024

#positive
sepal_length = tf[['sepal.length']]
print("Skewness: " , sepal_length.skew())
sepal_length.hist(column = ['sepal.length'], bins = 5)

#%%
#negative
petal_width = tf[['petal.width']]
print("Skewness: " , petal_length.skew())
petal_width.hist(column = ['petal.width'], bins = 5)

#%% problem 3
#Adri Saha
#2019-1-60-024

#positive
sepal_width = tf[['sepal.width']]
print("Kurtosis: " , sepal_width.kurt())
print("Skewness: " , sepal_width.skew())
tf.boxplot(column = ['sepal.width'])

#%%
#negative
petal_width = tf[['petal.width']]
print("Kurtosis: " , petal_length.kurt())
print("Skewness: " , petal_length.skew())
tf.boxplot(column = ['petal.length'])
#%%
#problem 4
#Adri Saha
#2019-1-60-024

tf['variety'].value_counts().plot(kind='bar')

#%%
tf['variety'].value_counts().plot(kind='pie')

#%%
#problem 5
#Adri Saha
#2019-1-60-024

print(tf.corr())

#%% problem 6
#Adri Saha
#2019-1-60-024

#positive
tf.plot.scatter(x='petal.length', y='petal.width')
#negative
tf.plot.scatter(x='sepal.width', y='petal.length')

#%% problem 7
#Adri Saha
#2019-1-60-024

import seaborn as sns
sns.heatmap(tf.corr(), cmap = sns.color_palette ("icefire", as_cmap = True), annot=True)



















