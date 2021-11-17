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


        
derivative = []
for j in range(len(volum)):
        deriverte_pH = (pH[j] - pH[j-1]) / (volum[j] - volum[j-1])
        j += 1
        derivative.append(deriverte_pH)
        
print(derivative)

def maximum_func(of_list):
    maximum = None
    for k in of_list:
        if (maximum is None or k > maximum):
            maximum = k
    return maximum

print(maximum_func(derivative))

class TestFunc(unittest.TestCase):
    def test_maximum(x):
        """
        Verify the values returned by function gjennomsnitt(liste):
            
            
        """
       
        x = derivative
        expected = np.max(derivative)
        computed = maximum_func(derivative)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"
        assert success, msg

        
if __name__ == '__main__':
    unittest.main()
    

