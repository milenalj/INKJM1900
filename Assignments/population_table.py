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


for t in np.arange(0, 49, step): #uniformely spaced range for t values
	N=B/(1+C*np.exp(-k*t))#population growth formula
	T.append(t) #adds values for time,t to the empty list
	N_values.append(N) # adds corresponding N values


#creating a table	

print ('--------------------------')
print ('t-values:      N_values:')
print ('--------------------------')

for t,N in zip(T,N_values):
    print('%.2f,          %.2f' % (t,N))	

print ('--------------------------')




# PROBLEM 3.7 IN ASSIGNMENT-OVERVIEW

#OUTPUT:

"""    
--------------------------
t-values:      N_values:
--------------------------
0.00,          5000.00
4.00,          9912.84
8.00,          17748.95
12.00,          27526.04
16.00,          36580.20
20.00,          42924.32
24.00,          46552.00
28.00,          48389.56
32.00,          49263.32
36.00,          49666.28
40.00,          49849.50
44.00,          49932.26
48.00,          49969.54
--------------------------
"""
