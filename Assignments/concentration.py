import sys
print(sys.version_info)

M = 158  # molar mass KMnO4 in g/mol
V = 1    # volume of solution in liters


user_input = input("Input mass of KMnO4 in grams or Enter to stop:")


def concentration(user_input):
    konsentrasjon = 0
    m = 0
    has_exception = False;
    
    #Try to cast to integer
    try:
        m = int(user_input)
    except ValueError:
        has_exception = True
    
    #Try to cast to float if not integer
    if (has_exception):
        try:
            m = float(user_input)
            has_exception = False
        except ValueError:
            has_exception = True
        
    #Wasn't integer nor float - raise error and exit
    if (has_exception):
        raise TypeError("The input must be a number")
        sys.exit()
        
    if m > 76:
        raise ValueError("The solubilty of KMnO4 is 76 g/L, the solution is saturated, input a lower number!")
        sys.exit()
    else:
        konsentrasjon = (m/M)/V
    return konsentrasjon


print("The concetration (molarity) of the KMnO4 solution is ", concentration(user_input), "M.")