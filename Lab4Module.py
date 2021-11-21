# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:32:51 2021

@author: Adri Saha
"""
#Name: Adri Saha
#ID: 2019-1-60-024
# Mean function for problem 4
def mean(a):
    total = 0
    count = 0
    for i in a:
        total= total+i
        count=count+1
    own_mean = total/count
    return own_mean
        