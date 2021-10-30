# -*- coding: utf-8 -*-
#Created on Wed Oct 27 21:18:12 2021

#@author: milenaljubisic

#Setter inn startbetingelser og importerer numpy, unittest og matplotlib:

import numpy as np
import matplotlib.pyplot as plt
import unittest


cal_conc = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5] #konsentrasjoner av kalibreringsløsninger i ppm
cal_abs = [0.0, 0.116, 0.216, 0.310, 0.425, 0.520] #absorbans for kalibreringsløsninger



def linear_regression(x, y):
    sum_x = 0
    sum_y = 0
    avg_x = np.mean(x)
    avg_y = np.mean(y)
    for i in x:
        var_x = (np.abs(avg_x - i))**2
        sum_x = sum_x + var_x
    for j in y:
        var_y = (np.abs(avg_y - j))**2
        sum_y = sum_y + var_y
    
    slope = sum_y/sum_x
    intercept = avg_y - (slope * avg_x)
    equation = (slope, intercept)
    return equation

test_x = np.arange(0.2, 1.0, 0.1)
test_y = np.arange(200.0, 360.0, 20)
print(test_y)

print(linear_regression(cal_conc, cal_abs))

class TestFunc(unittest.TestCase):
    def test_linear_regression(x, y):
        """
        Verify the values returned by function linear_regression():
            
            
        """
        x = test_x
        y = test_y
        
        expected = (200, 160)
        computed = linear_regression(cal_conc, cal_abs)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"
        assert success, msg



#print(test_linear_regression(avg_conc, avg_abs))

if __name__ == '__main__':
    unittest.main()
    

"""

def regression_bly(x):
    y = slope*x + intercept
    return y

print(regression_bly(0))


x = np.linspace(0, 0.6, 100)
#y = slope*x + intercept

plt.xlabel('Konsentrasjon av bly i vann (ppm)', color='black')
plt.ylabel('Absorbans', color='black')
plt.plot(cal_conc, cal_abs, 'ro')
plt.plot(x, regression_bly(x))
plt.show()

"""