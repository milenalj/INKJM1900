# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:33:39 2021

@author: milenaljubisic
"""
import numpy as np
import unittest


liste = [1,2,2,1,3,3]

def gjennomsnitt(liste):
    sum_gjennomsnitt = 0
    for i in liste:
        sum_gjennomsnitt += i
    verdi = sum_gjennomsnitt/len(liste)
    return verdi

print(gjennomsnitt(liste))

def standardavvik(liste):
    sum_stdavvik = 0
    for j in liste:
        sum_stdavvik += (j-gjennomsnitt(liste))**2
    verdi_stdavvik = np.sqrt(sum_stdavvik/len(liste))
    return verdi_stdavvik

print(standardavvik(liste))


class TestFunc(unittest.TestCase):
    def test_gjennomsnitt(x):
        """
        Verify the values returned by function gjennomsnitt(liste):
            
            
        """
       
        x = liste
        expected = np.mean(liste)
        computed = gjennomsnitt(liste)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"
        assert success, msg
    def test_stdavvik(y):
        """
        Verify the values returned by the function standardavvik(liste):
        
        
        """
        
        y = liste
        expected = np.std(liste)
        computed = standardavvik(liste)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed value={computed} != {expected}(expected)"
        assert success, msg
        
        
        
if __name__ == '__main__':
    unittest.main()
    