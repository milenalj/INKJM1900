# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:51:30 2021

Problem 4.4
@author: milenaljubisic
"""
import numpy as np
import unittest

A = (2,11)
B = (3,5)
C = (7,-5)
area = 0
vertices = [] #creating empty list of coordinates

vertices.append(A)
vertices.append(B)
vertices.append(C)


def  triangle_area(vertices):
    return 0.5*(np.abs((vertices[1][0]*vertices[2][1])- (vertices[2][0]*vertices[1][1])-(vertices[0][0]*vertices[2][1]) + (vertices[2][0]*vertices[0][1])+ (vertices[0][0]*vertices[1][1]) - (vertices[1][0]*vertices[0][1])))
class TestFunc(unittest.TestCase):
    def test_triangle_area(vertices):
        """
        Verify the area of a triangle with vertices
        (0,0), (1,0), and (0,2).
        """
        v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
        vertices = [v1, v2, v3]
        expected = 1
        computed = triangle_area(vertices)
        tol = 1E-14
        success = abs(expected - computed) < tol
        msg = f"computed area={computed} != {expected}(expected)"
        assert success, msg


if __name__ == '__main__':
    unittest.main()
    
    
"""
Output:
    
E
======================================================================
ERROR: test_triangle_area (__main__.TestFunc)
Verify the area of a triangle with vertices
----------------------------------------------------------------------
TypeError: test_triangle_area() takes 0 positional arguments but 1 was given

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (errors=1)


Når jeg endrer uttryket i linije 25 til å være def test_triangle_area(vertices):,
så får jeg:
    
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK


"""    
    