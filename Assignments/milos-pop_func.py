from math import e

t_values = []
N_values = []
n = 48

# function that calculates and returns value
def population(t,k,B,C):
    N = 5000
    n = 48
    return B/(1 + C*e**(-k*t))

# code that uses the function to populate array for time and array for calculated value
for t in range(0, (n+1), 2): #uniformely spaced range for t values
	N=population(t, 0.2, 50000, 9)
	t_values.append(t) #adds values for time,t to the empty list
	N_values.append(N) # adds corresponding N values

# code that prints two arrays as table
print("t-values:       N-values:")
for t,N in zip(t_values,N_values):
    print(f"{t:2f}        {N:2f}")
print("                         ")