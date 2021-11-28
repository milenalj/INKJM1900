# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 20:47:57 2021

@author: milenaljubisic
"""

import numpy as np
import matplotlib.pyplot as plt

dt = 0.001 # tidssteg
tid = 100 # tid i sekunder
N = int(tid/dt) # antall iterasjoner


# Startbetingelser:
M = 9.0e17 # konsentrasjon av en ikke-reagerende støtpartner
conc_O2 = 0.21 * M # konsentrasjon av molekylært oksygen (O2)
conc_O = 0 # konsentrasjon av oksygen
conc_O3 = 0 # konsentrasjon av ozon

# Konstanter:
k1 = 3.0e-12
k2 = 1.2e-33 
k3 = 5.5e-4
k4 = 6.9e-16

# likninger:
# delta_O = 2*k1*conc_O2 - k2*conc_O2*conc_O*M + k3*conc_O3 + k4*conc_O3*conc_O
# delta_O3 = k2*conc_O2*M - k3*conc_O3 - k4*conc_O*conc_O3

t = np.zeros(N)
O = np.zeros(N)
O2 = np.zeros(N)
O3 = np.zeros(N)

O[0] = conc_O
O2[0] = conc_O2
O3[0] = conc_O3


for i in range(N-1):
    O_derv = 2*k1*O2[i] - k2*O2[i]*O[i]*M + k3*O3[i] - k4*O3[i]*O[i]
    O2_derv = -k1*O2[i] - k2*O2[i]*O[i]*M + k3*O3[i] + 2*k4*O3[i]*O[i]
    O3_derv = k2*O2[i]*M - k3*O3[i] - k4*O[i]*O3[i]
    
    # Eulers metode
    O[i+1] = O[i] + O_derv*dt
    O2[i+1] = O2[i] + O2_derv*dt
    O3[i+1] = O3[i] + O3_derv*dt
    t[i+1] = t[i] + dt
    

plt.title('Produksjon og nedbrytning av ozon')
plt.yscale('log')
plt.xlabel('tid (s)')
plt.ylabel('Konsentrasjon (molec/cm$^3$)')
plt.plot(t, O, label = 'O')
#plt.plot(t, O2, label = 'O$_2$')
plt.plot(t, O3, label = 'O$_3$')
plt.legend()  

#odavde ne radi

from scipy.integrate import solve_ivp

t0 = 0
tid_slutt = 108
t = np.linspace(t0, tid_slutt, int(1E6))

def dO_dt(O, t):
    return 2*k1*O2 - k2*O2*O*M + k3*O3 - k4*O3*O

def dO2_dt(O2, t):
    return -k1*O2 - k2*O2*O*M + k3*O3 + 2*k4*O3*O

def dO3_dt(O3, t):
    return k2*O2*M - k3*O3 - k4*O*O3

print(dO3_dt(O3,t))

y0 = 0.21 * M
O2_int = solve_ivp(dO2_dt, [t0, tid_slutt], [0.21 * M], t_eval = t, method = 'BDF')

plt.xlabel("t")
plt.ylabel("y")
plt.plot(O2_int.O, O2_int.t[0])

plt.show()