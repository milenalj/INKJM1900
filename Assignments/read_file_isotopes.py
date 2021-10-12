# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 16:32:33 2021

@author: milenaljubisic
"""

isotopes = open(r"oxygen.txt","r")
line = isotopes.read().splitlines()
#items = line.split()
masses = []
abundance = []



print (line[1][2])



relative_mass = 0
i = 0
"""
for i from 1 to 4:
    x = isotopes.readline(i)
    m = x1[1]
    abundance = x1[2]
    relative_mass = relative_mass + m*abundance
    x = isotopes.readline(i+1)

print (relative_mass)
print (x)
"""
