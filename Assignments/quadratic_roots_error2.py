# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:21:06 2021

@author: milenaljubisic
"""

import numpy as np



a = float(input('Value of coefficient a:'))
b = float(input('Value of coefficient b:'))
c = float(input('Value of coefficient c:'))

def quadratic(a, b, c):
    if b**2 - 4*a*c < 0:
        raise ValueError('These coefficients give results with complex roots!')
        sys.exit(1)
    else:
        x1 = (-b + np.sqrt(b**2 - 4*a*c))/2*a
        x2 = (-b - np.sqrt(b**2 - 4*a*c))/2*a
        return x1, x2


print ("The solutions to the equation are"  ' %.2f,  %.2f.' % quadratic(a, b, c))






#OUTPUT:
    
#runfile('C:/Users/milenaljubisic/Documents/INKJM1900/Assignments/quadratic_roots_error2.py', wdir='C:/Users/milenaljubisic/Documents/INKJM1900/Assignments')

#Value of coefficient a:1

#Value of coefficient b:1

#Value of coefficient c:1
#Traceback (most recent call last):

  #File "C:\Users\milenaljubisic\Documents\INKJM1900\Assignments\quadratic_roots_error2.py", line 26, in <module>
    #print ("The solutions to the equation are"  ' %.2f,  %.2f.' % quadratic(a, b, c))

  #File "C:\Users\milenaljubisic\Documents\INKJM1900\Assignments\quadratic_roots_error2.py", line 18, in quadratic
    #raise ValueError('These coefficients give results with complex roots!')

#ValueError: These coefficients give results with complex roots!

#runfile('C:/Users/milenaljubisic/Documents/INKJM1900/Assignments/quadratic_roots_error2.py', wdir='C:/Users/milenaljubisic/Documents/INKJM1900/Assignments')

#Value of coefficient a:1

#Value of coefficient b:0

#Value of coefficient c:-1
#The solutions to the equation are 1.00,  -1.00.
