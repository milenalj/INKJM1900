# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:17:40 2021

@author: milenaljubisic
"""

import unittest
# PV = nRT, ideal gas equation


def get_pressure(V, n, T, R = 8.314):
    """
    Function that returns the pressure of an ideal gas, given temperature, volume,
    amount of gas in moles and the ideal gas constant with the standard value of R = 8,314 J/(K x mol).
    
    Parameters
    ----------
    V : volume
        Volume of the gas in m^3.
        
    n : amount
        Amount of gas in moles.
        
    T : temperature
        The temperature of gas in Kelvin (K).
        
    R : ideal gas constant
        Stopping condition, when stop > abs_value(f(x)).
        
    maxteration : integer
        ideal gas constant with the standard value of R = 8,314 J/(K x mol).

    Returns
    -------
    P: pressure
    
    Pressure in Pascal (Pa).
    """
    
    P = (n * R * T)/V
    
    return P

get_pressure(0.03, 1, 273)


class TestFunc(unittest.TestCase):
    
    def test_pressure (V_test, n_test, T_test):
        """
        Testing for standard conditions of:
        
        V_test = 0.022414 
        T_test = 273.15   : standard atmospheric temperature
        n_test = 1
        
        """
        V_test = 0.022414 
        n_test = 1
        T_test = 273.15
        expected = 101.325 * 1000
        computed = get_pressure(V_test, n_test, T_test)
        tol = 1E-10
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"

if __name__ == '__main__':
    unittest.main()
    