import numpy as np
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:23:34 2021

@author: milenaljubisic
"""

K_a =1.50e-04
volume_acid = 0.0100
volume_base = 0.03352
concentration_base = 0.500
K_w = 1.00e-14
V_total = volume_acid + volume_base

#pH of acid before base addition:
pH_syre = 2.51
conc_syre_start = 10**(-pH_syre)
n_glykolsyre = conc_syre_start*volume_acid

print(n_glykolsyre)

K_b = 6.67E-11
c_glykolsyre_ekv = n_glykolsyre/V_total
c_OH = np.sqrt(K_b*c_glykolsyre_ekv)
pOH = -np.log10(c_OH)
pH = 14-pOH
print(f'pH ved ekvivalenspunktet er {pH}')
