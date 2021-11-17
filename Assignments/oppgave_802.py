import numpy as np
import matplotlib.pyplot as plt
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 17:23:34 2021

@author: milenaljubisic
"""

K_a = 1.50e-04
V_a = 0.0100
V_b = 0.03352
c_b = 0.500
K_w = 1.00e-14
V_t = V_a + V_b

#pH of acid before base addition:
pH_syre = 2.51
c_a = 10**(-pH_syre)
n_glykolsyre = c_a*V_a


K_b = 6.67E-11
c_glykolsyre_ekv = n_glykolsyre/V_t
c_OH = np.sqrt(K_b*c_glykolsyre_ekv)
pOH = -np.log10(c_OH)
pH = 14-pOH
print(f'pH ved ekvivalenspunktet er {pH}')

def get_acid_conc(hydrogen):
    return V_t*(hydrogen + K_a)*hydrogen**2 + c_b*V_b*(hydrogen + K_a)*hydrogen - K_w*V_t*(hydrogen + K_a) - c_a*V_a*K_a*hydrogen

hydrogen1 = np.linspace(-1, 1, 101)
hydrogen2 = np.linspace(-1.0e-8,1.0e-8, 101)



#plt.plot(hydrogen1, get_acid_conc(hydrogen1), color='blue', label='Acid concentration - 1')
plt.plot(hydrogen2, get_acid_conc(hydrogen2), color='red', label='Acid concentration - 2')
plt.legend() 
plt.show()

def newtons_method(f, df, a, stop, max_iteration):
    
    """
    Function that returns the roots of a function for f(x) = 0.
    
    Parameters
    ----------
    f : function
        Function for which the roots should be found.
        
    df : function
        The derivative of function f, f'(x).
        
    a : float
        Initial guess for one of the roots.
        
    stop : float
        Stopping condition, when stop > abs_value(f(x)).
        
    maxteration : integer
        Maximum number of iterations.

    Returns
    -------
    x.
    
    """
    
    x = a
    
    for i in range(0, max_iteration):
        fx = f(x)
        if abs(fx) < stop:
            print('Found a solution after',i,'iterations.')
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError('Zero derivative. No solution found.')
            return None
        x = x - fx/dfx
    raise ValueError('Exceeded maximum iterations. No solution found.')
    return None
    

f = lambda x_i: V_t*(x_i + K_a)*x_i**2 + c_b*V_b*(x_i + K_a)*x_i - K_w*V_t*(x_i + K_a) - c_a*V_a*K_a*x_i
df = lambda x_i: 3*V_t*x_i**2 + 2*V_t*K_a*x_i + 2*c_b*V_b*x_i + c_b*V_b*K_a - K_w*V_t - K_w*V_t*K_a - c_a*V_a*K_a

result = newtons_method(f,df,0.1,1e-10,100)
print(result) 