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
    return slope, intercept

slope, intercept = linear_regression(cal_conc, cal_abs)
linear_regression(cal_conc, cal_abs)

def regression_abs(concentration):
    absorbance = slope*concentration + intercept
    return absorbance

concentration = np.linspace(0, 0.6, 100)

plt.xlabel('Konsentrasjon av bly i vann (ppm)', color='black')
plt.ylabel('Absorbans', color='black')
plt.plot(cal_conc, cal_abs, 'ro')
plt.plot(concentration, regression_abs(concentration))
plt.show()

abs = 0.340
def regression_conc(abs):
    value = (abs + intercept)/slope
    return value


concentration_of_ions = regression_conc(abs)
print("Konsentrasjon av blyioner i vannet er %.2f ppm" %concentration_of_ions)






