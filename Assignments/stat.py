# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:45:13 2021

@author: milenaljubisic
"""

import numpy as np
import unittest

x_values = [0.699, 0.703, 0.698, 0.688, 0.701]
 
def mean (x_values):
    s = 0
    for i in x_values:
        s = s + i
    return s/len(x_values)
    
class TestFunc(unittest.TestCase):
    def test_mean (x_values):
        """
        Compare the means computed by function mean (x_values) and np.mean
        
        """
        x_values = [0.699, 0.703, 0.698, 0.688, 0.701]
        expected = np.mean(x_values)
        computed = mean(x_values)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"

if __name__ == '__main__':
    unittest.main()
    

"""
Output:

----------------------------------------------------------------------
Ran 1 test in 0.009s

OK

"""