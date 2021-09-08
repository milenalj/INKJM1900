from math import e

B=50000 #carrying capacity

k=0.2 #growth rate per hour

N=5000 #start population

t= 0

C=9.0  #coefficient calculated from population.py

T=[] #empty list of t-values

N_values=[] #empty list of number of bacteria at given given time, t

n=12

for t in range(0, (n+1), 2): #uniformely spaced range for t values

	N=B/(1+C*e**(-k*t))#population growth formula

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
2.00,          7109.46
4.00,          9912.84
6.00,          13474.37
8.00,          17748.95
10.00,          22542.65
12.00,          27526.04
--------------------------
"""
