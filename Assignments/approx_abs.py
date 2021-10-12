# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:01:25 2021

@author: milenaljubisic
"""

import numpy as np 
import matplotlib.pyplot as plt 
 
 
 
x_values = np.linspace(-np.pi, np.pi, 101) 
n_values = [1, 2, 3, 4] 

 
def abs_approx(x, n): 
    s = 0  
    y_values = [] 
    for n in range(1, n+1): 
        s = s + (np.cos((2*n-1)*x)/(2*n-1)**2) 
        value = np.pi/2 - (4/np.pi)*s 
        y_values = np.array(value)
    return y_values  
 
#print(abs_approx(x_values, 4)) 
#print(len(abs_approx(x_values, 4))) 

 
def exact_value(x): 
    return np.absolute(x) 
 
plt.plot(x_values, exact_value(x_values), color='red', label='Exact value') 
 
for n in n_values: 
    plt.plot(x_values, abs_approx(x_values, n), label='N = %d' %n) 
 

 
 
plt.xlim([-np.pi, np.pi])
plt.ylim([0, 3.5])  
plt.legend() 
plt.show()