# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:17:40 2021

@author: milenaljubisic
"""

import unittest
# PV = nRT, ideal gas equation


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
def get_pressure(V, n, T, R = 8.314472):
    P = (n * R * T)/V
    return P


class TestFunc(unittest.TestCase):
    
    def test_pressure (self):
        """
        Testing for standard conditions of:
        
        V_test = 0.022414 
        T_test = 273.15   : standard atmospheric temperature
        n_test = 1
        
        """
        
        V_test = 0.022414 
        n_test = 1
        T_test = 273.15
        calculated_result = get_pressure(V_test, n_test, T_test)
        expected_result = 101324.9
        tol = 0.08
        self.assertTrue(abs(expected_result - calculated_result ) < tol)

if __name__ == '__main__':
    unittest.main()
    