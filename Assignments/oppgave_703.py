# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:20:11 2021

@author: milenaljubisic
"""

import pandas as pd
import numpy as np

file = pd.read_csv ('vin.csv')

correlation_coefficients = [] 

def get_correlation(file, i):
    col_i = file.iloc[:,i]
    col_j = file.iloc[:,11]
    avg_i = np.mean(col_i)
    avg_j = np.mean(col_j)
    
    top = []
    bottom_i = []
    bottom_j = []
    sum_top = 0
    
    for x in range(0,len(col_i)):
        top.append((col_i[x] - avg_i)*(col_j[x] - avg_j))
        bottom_i.append((col_i[x] - avg_i)**2)
        bottom_j.append((col_j[x] - avg_j)**2)
        
    sum_top = np.sum(top)
    sum_bottom = np.sqrt(np.sum(bottom_i) * np.sum(bottom_j))

    return sum_top/sum_bottom



    

for i in range(0, 11):
   column = []
   x = get_correlation(file, i)
   column.append(x)
   correlation_coefficients.append(column) 
   
   

print(correlation_coefficients)
        