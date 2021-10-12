# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 18:30:06 2021

@author: milenaljubisic
"""
import matplotlib.pyplot as plt
import numpy as np
import re


x_values = []
y_values = []
points = []


def input_coordinates():
    a = input("Input coordinates in format x,y or Enter to stop:")
    if not a:
        return False
    x = check_input(a)
    p1 = tuple(int(x) for x in a.split(','))
    points.append(p1)
    return True

def check_input(text):
    x = re.search("[0-9]+,[0-9]+", text)
    if x:
        return True
    else:
        print ("Enter coordinates in format x,y")
        raise ValueError
        
def plot_line(p1, p2):
    x_values.extend([p1[0], p2[0]])
    y_values.extend([p1[1], p2[1]])
    plt.plot(x_values, y_values)

def complete_graph(points):
    for i in range(0,len(points)):
        for j in range (i+1, len(points)):
            plot_line(points[i], points[j])
    return plt.show()

def alpha_test():
    alpha = np.sqrt(2)/2
    alpha_points = [(1,0),(alpha,alpha),(0,1),(-alpha,alpha),(-1,0),(-alpha,-alpha),(0,-1),(alpha,-alpha)]
    complete_graph(alpha_points)
    

while True:
    if not input_coordinates():
        break

# Uncomment function below and comment out alpha_test in order to test
# manual input of coordinates from part a)
#complete_graph(points)   


# Uncomment function below and comment out complete_graph in order to test
# example from part b)
alpha_test()