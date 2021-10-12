# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:02:51 2021

@author: milenaljubisic
"""
sequence = []
nr_terms = 13
xn1 = xn2 = 1
i = 0

sequence.append(xn1)
sequence.append(xn2)

while i < nr_terms:
    x = xn1 + xn2
    xn1 = xn2
    sequence.append(x)
    xn2 = x
    i += 1
    
print(sequence)


"""
OUTPUT:
    
runfile('C:/Users/milenaljubisic/Documents/INKJM1900/Assignments/fibonacci.py', wdir='C:/Users/milenaljubisic/Documents/INKJM1900/Assignments')
[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
       
"""