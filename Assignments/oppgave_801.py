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
count = 1
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


#def derivative_pH(volume, pH_value):
    #for j in range(0, len(volume)):
        
derivative = []
for j in range(1, len(volum)+2):
        deriverte_pH = (pH[j] - pH[j-1]) / (volum[j] - volum[j-1])
        j += 1
        derivative.append(deriverte_pH)
        #print(pH)

print(derivative)

#with open('titreringsdata.txt', 'a') as 


