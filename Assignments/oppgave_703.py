# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:20:11 2021

@author: milenaljubisic
"""

import pandas as pd


file = pd.read_csv ('vin.csv')
print (file)


correlation_coefficients = []

def get_correlation(file, i, j):
    lo
    return file.iat[j, i]
    

for i in range(0, 12):
    column = []
    for j in range(0, 1598):
        #print(i, j)
        
        x = get_correlation(file, i, j)
        column.append(x)
    correlation_coefficients.append(column)  

print(correlation_coefficients)
        