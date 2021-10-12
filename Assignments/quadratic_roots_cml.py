# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 15:33:38 2021

@author: milenaljubisic
"""

import numpy as np
import sys



a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

def quadratic(a, b, c):
    x1 = (-b + np.sqrt(b**2 - 4*a*c))/2*a
    x2 = (-b - np.sqrt(b**2 - 4*a*c))/2*a
    return x1, x2


print ("The solutions to the equation are"  ' %.2f,  %.2f.' % quadratic(a, b, c))


#OUTPUT:
    

#C:\Users\milenaljubisic\Documents\INKJM1900\Assignments>python quadratic_roots_cml.py 1 4 1
#The solutions to the equation are -0.27,  -3.73.
