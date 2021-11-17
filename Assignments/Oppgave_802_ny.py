import numpy as np
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:23:34 2021

@author: milenaljubisic
"""

K_a =1.50e-04
V_b = 0.03352 # volume base
c_b = 0.500 # concentration base
V_a = 0.0100 # volume acid
c_a = 0.00309 # concentratoin acid
K_w = 1.00e-14
V_t = V_a + V_b


def hidrogen_concentration_func():
    numerator = -c_b*V_b+np.sqrt(c_b**2*V_b**2 + 4*V_t**2*K_w + 4*V_t*c_a*V_a*K_a - 4*V_t*c_a*V_a*K_a**2)
    denominator = 4*V_t
    return numerator/denominator


test = hidrogen_concentration_func()

print(test)
