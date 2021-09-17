# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:44:13 2021

@author: milenaljubisic
"""
import numpy as np
import unittest

def f(x):
    if np.sin(x) > 0:
        return np.sin(x)
    elif np.sin(x) <= 0:
        return 0
    
class TestFunc(unittest.TestCase):
    def test_positive(x):
        """
        Verify the values returned by function f(x) for x = pi/2
        
        """
        x = np.pi/2
        expected = 1
        computed = f(x)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"
        assert success, msg
    def test_negative(x):
        """
        Verify the values returned by function f(x) for x = 3* pi/2:
            
    

        """
        x = 3*np.pi/2
        expected = 0
        computed = f(x)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"
        assert success, msg
      
        
        
        
if __name__ == '__main__':
    unittest.main()
    
"""
Output:
    
----------------------------------------------------------------------
Ran 2 tests in 0.002s

OK

"""