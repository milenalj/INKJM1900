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

print(x0, x1, x2)

#numpy_pi = np.pi

"""
print("-------------------------------------------------")
print("The value of pi from numpy is: %.13f" %numpy_pi)
print("-------------------------------------------------")
#print("The value of x0 is: %.13f"%x0)
print("-------------------------------------------------")
"""