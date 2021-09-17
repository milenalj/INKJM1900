    import numpy as np

t_values = []  #defining empty list of t-values
N_values = []  #defining empty list of N-values
t = 0
k = 0.2 #growth rate per hour
B = 50000  #carrying capacity
C = 9  #coefficient calculated from population.py
N = 5000 #start population
n = 12
step = 48/n

def population(t,k,B,C):
    return B/(1 + C*np.exp(-k*t))

for t in np.arange(0, 49, step): #uniformely spaced range for t values
        N = population(t, k, B, C) 
        t_values.append(t)
        N_values.append(N)


#creating a table	

print ('--------------------------')
print("t-values:       N-values:")
print ('--------------------------')
for t,N in zip(t_values,N_values):
    print('%.2f,        %.2f' % (t,N))
print ('--------------------------')




"""
OUTPUT:
    
--------------------------
t-values:       N-values:
--------------------------
0.00,        5000.00
4.00,        9912.84
8.00,        17748.95
12.00,        27526.04
16.00,        36580.20
20.00,        42924.32
24.00,        46552.00
28.00,        48389.56
32.00,        49263.32
36.00,        49666.28
40.00,        49849.50
44.00,        49932.26
48.00,        49969.54
--------------------------



"""