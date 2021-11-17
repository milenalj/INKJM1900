# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 12:44:57 2021

@author: milenaljubisic
"""

import numpy as np
import matplotlib.pyplot as plt
import unittest


lines = []

with open('titreringsdata.txt', 'r') as data:
    lines = data.readlines()

volum = []
pH = []

for i in range(1, len(lines)):
    x, y = map(float, lines[i].split(","))
    volum.append(x)
    pH.append(y)
    i += 1
    

#print(volum)
#print(pH)

plt.plot(volum, pH, color='blue', label='Titreringskurven')
plt.plot(volum, pH, 'bo')

plt.xlim([-5, 55])
plt.ylim([2, 13])  
plt.legend() 
plt.show()  

data.close()

"""
Input is matrix in format
[derivative1, pH1, volume1]
[derivative2, pH2, volume2]
[derivative_n, pH_n, volume_n]
"""
def getdata_with_max_derivative_func(data_matrix):
    maximum = 0
    row_with_max = []
    for row in data_matrix:
        if (row[0] > maximum):
            maximum = row[0]
            row_with_max = row
    return row_with_max

        
derivative = []
data_matrix = []
for j in range(len(volum)):
        deriverte_pH = (pH[j] - pH[j-1]) / (volum[j] - volum[j-1])
        data_matrix.append([deriverte_pH, pH[j], volum[j]])
        derivative.append(deriverte_pH)
        j += 1
        
max_data = getdata_with_max_derivative_func(data_matrix)


print()
print("Discovered max: ", max_data[0], "- compared to numpy.max: ", np.max(derivative))
print("For pH =",max_data[1], "and volume =",max_data[2])
