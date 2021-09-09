# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:47:26 2021

@author: milenaljubisic
"""

s_1 = 0
s_2 = 0
M = 3
k = 1

while k <= M:
     s_1 += 1/(2*k)**2
     k = k+1




for k in range(1, M+1):
    s_2 += 1/(2*k)**2
    
    
if s_1 == s_2:
    print ('The sums are equal.')
else:
    print ('The sums are not equal.')


#OUTPUT:

"""
The sums are equal.

"""