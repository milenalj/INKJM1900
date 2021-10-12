# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:58:44 2021

@author: milenaljubisic
"""

import numpy as np
import sys


try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

except IndexError:
    print ('You failed to input all of the coefficients, input missing data:')
    a = float(input('Value of coefficient a:'))
    b = float(input('Value of coefficient b:'))
    c = float(input('Value of coefficient c:'))
    



def quadratic(a, b, c):
    x1 = (-b + np.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - np.sqrt(b**2 - 4*a*c))/2*a
    return  x1, x2
    
    
print ("The solutions to the equation are"  ' %.2f,  %.2f.' % quadratic(a, b, c))



"""
OUTPUT:
    
C:\Users\milenaljubisic\Documents\INKJM1900\Assignments>python quadratic_roots_error.py 1 3
You failed to input all of the coefficients, input missing data:
Value of coefficient a:1
Value of coefficient b:4
Value of coefficient c:1
The solutions to the equation are -0.27,  -3.73.

"""