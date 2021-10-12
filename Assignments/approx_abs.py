# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 12:08:59 2021

@author: milenaljubisic
"""

import numpy as np
import matplotlib.pyplot as plt



x_values = np.linspace(-np.pi, np.pi, 101)
n_values = [1, 2, 3, 4]
#y_values = []

def abs_approx(x, n):
    s = 0 
    for n in n_values:
        s = s + (np.cos((2*n-1)*x)/(2*n-1)**2)
        value = np.pi/2 - (4/np.pi)*s
        y_values = np.array(value)
        #y_values.append(value)
        n = n + 1
    return y_values

print(abs_approx(x_values, 2))
print(len(abs_approx(x_values, 2)))

"""

def abs_approx(x, n):
    k = np.arange(n)
    X, K = np.meshgrid(x, k)
    val = np.pi/2 - ((4/np.pi)*(np.cos((2*K -1)*X)/(2*K -1)**2)
    return np.sum(val, axis=0)

"""


def exact_value(x):
    return np.absolute(x)

plt.plot(x_values, exact_value(x_values), color='red', label='Exact value')
plt.plot(x_values, abs_approx(x_values, 4), color='blue', label='Exact value')

#for n in [1, 2, 3, 4]:
    #plt.plot(x, abs_approx(x, n), label='N = 'str(k))

#print(abs_approx(x_values, 1))

#plt.plot(x_values, abs_approx(x_values, 4), color='blue', label='N=1')


plt.xlim([-np.pi, np.pi])
plt.legend()
plt.show()