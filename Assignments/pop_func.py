from math import exp

t_values = []
N_values = []

def population(t,k,B,C):
    t = 0
    k = 0.2
    B = 50000
    C = 9
    N = 5000
    n = 48
    for t in range(0,(n+1),2):
        t_values.append(t)
        N_values.append(N)
    return B/(1 + C*exp**(-k*t))

print("t-values:       N-values:")
for t,N in zip(t_values,N_values):
    print(f"{t:2f}        {N:2f}")
print("                         ")
