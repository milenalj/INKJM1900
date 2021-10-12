# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:17:53 2021

@author: milenaljubisic
"""
import numpy as np

x0 = 3.14

def newton_pi(x):
    next_x = x - (np.sin(x)/np.cos(x))
    return next_x

x1 = newton_pi(x0)
x2 = newton_pi(x1)


numpy_pi = np.pi


print("-------------------------------------------------")
print("The value of pi from numpy is: %.13f" %numpy_pi)
print("-------------------------------------------------")
print("The value of x0 is: %.13f" %x0)
print("-------------------------------------------------")
print("The value of x1 is: %.13f" %x1)
print("-------------------------------------------------")
print("The value of x2 is: %.13f" %x2)
print("-------------------------------------------------")


"""
OUTPUT:
    
runfile('C:/Users/milenaljubisic/Documents/INKJM1900/Assignments/finding_pi.py', wdir='C:/Users/milenaljubisic/Documents/INKJM1900/Assignments')
-------------------------------------------------
The value of pi from numpy is: 3.1415926535898
-------------------------------------------------
The value of x0 is: 3.1400000000000
-------------------------------------------------
The value of x1 is: 3.1415926549364
-------------------------------------------------
The value of x2 is: 3.1415926535898
-------------------------------------------------


"""