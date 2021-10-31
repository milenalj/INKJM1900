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
    #suma kolone 0
    #suma kolene 1
    avg_i = np.mean(file.iloc[:,i])
    avg_j = np.mean(file.iloc[:,i+1])
    print(avg_i, avg_j)
    
    return avg_i
    

for i in range(0, 11):
   column = []
   x = get_correlation(file, i)
   column.append(x)
   correlation_coefficients.append(column) 
   


#print(correlation_coefficients)
        