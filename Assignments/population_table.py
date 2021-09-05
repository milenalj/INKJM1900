from math import e
B=50000 #carrying capacity
k=0.2 #growth rate per hour
N=5000 #start population
t=0
C=9.0  #oefficient calculated from population.py
T=[] #empty list of t-values
N_values=[] #empty list of number of bacteria at given given time, t
n=48
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



