import numpy as np

def T_array_AD(g):
    if  1. <= g  <= 30.:
        f = np.arange(1e-1, 1.01, 1e-2)
    elif  40 <= g <= 2e+3:
        f = np.arange(1, 10.1, 1e-1)
    elif  3e+3 <= g <= 3e+5:
        f = np.arange(10, 101, 1) 
    elif  4e+3 <= g <= 1e+6:
        f = np.arange(100, 1010, 10)       
    else:
        print('error: unknown value of g')    
    return f

def T_array_AD_test(g):
    if  1. <= g  <= 30.:
        f = np.arange(1e-1, 1.01, 1e-2)
    elif  40. <= g <= 2e+3:
        f = np.arange(1., 10.01, 1e-2)
    else:    
        print('error: unknown value of g')    
    return f