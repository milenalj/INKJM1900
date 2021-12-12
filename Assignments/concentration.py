import sys

M = 158  # molar mass KMnO4 in g/mol
V = 1    # volume of solution in liters


m = eval(input("Input mass of KMnO4 in grams or Enter to stop:"))


def concentration(m):    
    if type(m) == str:
        raise TypeError("The input must be a number")
        print(quit)
        quit()
    if type(m) == float:
        pass
    if type(m) == int:
        pass
    elif m > 76:
        raise ValueError("The solubilty of KMnO4 is 76 g/L, the solution is saturated, input a lower number!")
        print(quit)
        quit()
    else:
        konsentrasjon = (m/M)/1
    return konsentrasjon

concentration(m)

print("The concetration (molarity) of the KMnO4 solution is ", concentration(m), "M.")