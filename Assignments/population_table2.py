# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 00:13:02 2021

@author: milenaljubisic
"""

from math import e
import numpy as np


B=50000 #carrying capacity
k=0.2 #growth rate per hour
N=5000 #start population
t= 0
C=9.0  #coefficient calculated from population.py
n=12
step = 48/n

T=[] #empty list of t-values
N_values=[] #empty list of number of bacteria at given given time, t
tN1 = [] #empty list for both t and N values

for t in np.arange(0, 49, step): #uniformely spaced range for t values
	N=B/(1+C*e**(-k*t))#population growth formula
	T.append(t) #adds values for time,t to the empty list
	N_values.append(N) # adds corresponding N values
    
tN1.append(T)
tN1.append(N_values)

#creating a table	

print ('--------------------------')
print ('t-values:      N_values:')
print ('--------------------------')

for t in tN1[0]:
    for N in tN1[1]:
        print(int(t),             int(N))
        t = t+step

#ne mogu da provalim kako da zaustavim loop za N
    
        
	   

print ('--------------------------')



#print (tN1[0])
#print (tN1[1])