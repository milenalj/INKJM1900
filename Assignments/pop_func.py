from math import e

t_values = []
N_values = []
t = 0
k = 0.2
B = 50000
C = 9
N = 5000
n = 48

def population(t,k,B,C):
    return B/(1 + C*e**(-k*t))

for t in range(0,(n+1),2):
        N = population(t, k, B, C)
        t_values.append(t)
        N_values.append(N)


print("t-values:       N-values:")
for t,N in zip(t_values,N_values):
    print('%.2f,        %.2f' % (t,N))
print("                         ")




