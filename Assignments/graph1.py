# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:30:06 2021

@author: milenaljubisic
"""
import matplotlib.pyplot as plt
import sys

x_values = []
y_values = []

a = input("Input coordinates for tuple p1:")
p1 = tuple(int(x) for x in a.split())
#view this tuple

if len(p1)>2:
    print ("Too many coordinates in the tuple, there should be 2.")
    raise ValueError
elif len(p1)<2:
    print("Missing coordinates, there should be 2.")
    raise ValueError
else:
    pass 

b = input("Input coordinates for tuple p2:")
p2 = tuple(int(x) for x in b.split())
#print(p2)


if len(p2)>2:
    print ("Too many coordinates in the tuple, there should be 2.")
    raise ValueError
elif len(p2)<2:
    print("Missing coordinates, there should be 2.")
    raise ValueError
else:
    pass

print(p1[0])
print(p2)

def plot_line(p1, p2):
    x_values.append(p1[0], p2[0])
    y_values.append(p1[1], p2[1])
    #y_values = [p1[1], p2[1]]
    plt.plot(x_values, y_values)
    return plt.show

plt.plot(x_values, y_values)
plt.show