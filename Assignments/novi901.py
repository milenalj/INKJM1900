# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 21:18:51 2021

@author: milenaljubisic
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


# Startbetingelser:
M = 9.0e17 # konsentrasjon av en ikke-reagerende støtpartner
O2 = 0.21 * M # konsentrasjon av molekylært oksygen (O2)
O = 0 # konsentrasjon av oksygen
O3 = 0 # konsentrasjon av ozon

k1 = 3.0e-12
k2 = 1.2e-33 
k3 = 5.5e-4
k4 = 6.9e-16


def ratelover(t,y):
    O = y[0]
    O2 = y[1]
    O3 = y[2]
    dO_dt = 2*k1*O2 - k2*O2*O*M + k3*O3 - k4*O3*O
    dO2_dt = -k1*O2 - k2*O2*O*M + k3*O3 + 2*k4*O3*O
    dO3_dt = k2*O2*M - k3*O3 - k4*O*O3
    return [dO_dt, dO2_dt, dO3_dt]

# def dO_dt(O, t):
#     return 2*k1*O2 - k2*O2*O*M + k3*O3 - k4*O3*O

# def dO2_dt(O2, t):
#     return -k1*O2 - k2*O2*O*M + k3*O3 + 2*k4*O3*O

# def dO3_dt(O3, t):
#     return k2*O2*M - k3*O3 - k4*O*O3


a = 0
b = 108
t = np.linspace(a,b,int(1E6))
y0 = [0.21 * M, 0, 0] # Array med startverdier
y_int = solve_ivp(ratelover, [a,b], y0, t_eval=t)

plt.xlabel("t (s)")
#plt.yscale('log')
plt.ylabel("c (mol/L)")
plt.plot(y_int.t, y_int.y[0]) # Plotter [HI]
plt.plot(y_int.t, y_int.y[2]) # Plotter [H2]
plt.show()


print(ratelover(t, y0))


# y0 = 0.21 * M
# O2_int = solve_ivp(dO2_dt, [t0, tid_slutt], [1], t_eval = t, method = 'BDF')

# plt.xlabel("t")
# plt.ylabel("y")
# plt.plot(O2_int.O, O2_int.t[0])

# plt.show()