# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 23:45:47 2021

@author: milenaljubisic
"""

M_C = 12.011 #molar mass of carbon
M_H = 1.0079 #molar mass of hydrogen

mass = 0
m = 0

for n in range(2, 10):
    m = 2 * n +2
    mass = n*M_C + m*M_H
    output = f"(C{n}H{m}) = {mass:.3f} g/mol."
    print (output)
    
    
    
"""
OUTPUT:
    
(C2H6) = 30.069 g/mol.
(C3H8) = 44.096 g/mol.
(C4H10) = 58.123 g/mol.
(C5H12) = 72.150 g/mol.
(C6H14) = 86.177 g/mol.
(C7H16) = 100.203 g/mol.
(C8H18) = 114.230 g/mol.
(C9H20) = 128.257 g/mol.    

"""