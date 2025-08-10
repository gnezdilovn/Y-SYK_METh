import numpy as np

def T_array(g, a):
    if a == 1e-3:
        #if g == 0.07:
        #    f = np.arange(1e-7, 101e-8, 1e-8)
        if g <= 0.08:
            f = np.arange(1e-6, 101e-7, 1e-7)
        elif  0.09 <= g <= 0.5:
            f = np.arange(1e-5, 101e-6, 1e-6)
        elif  0.6 <= g <= 30.0:
            f = np.arange(1e-4, 101e-5, 1e-5)   
        elif  40.0 <= g <= 4e+3:
            f = np.arange(1e-3, 101e-4, 1e-4)
        elif  5e+3 <= g:
            f = np.arange(1e-2, 1e-1, 1e-3)    
        else:
            print('error: unknown value of g')
    elif a == 1e-2:
        #if 0.07 <= g <= 0.08:
        #    f = np.arange(1e-6, 101e-7, 1e-7)
        if  g <= 0.08:
            f = np.arange(1e-5, 101e-6, 1e-6)
        elif  0.09 <= g <= 0.5:
            f = np.arange(1e-4, 101e-5, 1e-5)
        elif  0.6 <= g <= 40.0:
            f = np.arange(1e-3, 101e-4, 1e-4)
        elif  50. <= g:
            f = np.arange(1e-2, 1e-1, 1e-3)    
        else:
            print('error: unknown value of g')
    elif a == 1e-1:
        #if 0.07 <= g <= 0.09:
        #    f = np.arange(1e-5, 101e-6, 1e-6)
        if  g <= 0.09:
            f = np.arange(1e-4, 101e-5, 1e-5)
        elif  0.1 <= g <= 0.7:
            f = np.arange(1e-3, 101e-4, 1e-4)
        elif  0.8 <= g:
            f = np.arange(1e-2, 1e-1, 1e-3)    
        else:
            print('error: unknown value of g')
    elif a == 1:
        #if 0.07 <= g <= 0.08:
        #    f = np.arange(1e-5, 101e-6, 1e-6)
        if g <= 0.05:
            f = np.arange(1e-4, 101e-5, 1e-5)
        elif 0.06 <= g <= 0.1:
            f = np.arange(1e-3, 101e-4, 1e-4)
        elif  0.2 <= g:
            f = np.arange(1e-2, 1e-1, 1e-3)
        else:
            print('error: unknown value of g') 
    elif a >= 10:
        #if 0.07 <= g <= 0.08:
        #    f = np.arange(1e-5, 101e-6, 1e-6)
        if g <= 0.04:
            f = np.arange(1e-4, 101e-5, 1e-5)
        elif 0.05 <= g <= 0.1:
            f = np.arange(1e-3, 101e-4, 1e-4)
        elif  0.2 <= g:
            f = np.arange(1e-2, 1e-1, 1e-3)
        else:
            print('error: unknown value of g')            
    #elif a == 10:
        #if 0.07 <= g <= 0.08:
        #    f = np.arange(1e-5, 101e-6, 1e-6)
        #elif 0.09 <= g <= 0.1:
        #    f = np.arange(1e-4, 101e-5, 1e-5)
    #    if g <= 0.1:
    #        f = np.arange(1e-3, 101e-4, 1e-4)
    #    elif  0.2 <= g:
    #        f = np.arange(1e-2, 1e-1, 1e-3)
    #    else:
    #        print('error: unknown value of g')
    #elif a == 100:
    #    if 0.07 <= g <= 0.08:
    #        f = np.arange(1e-5, 101e-6, 1e-6)
    #    elif 0.09 <= g <= 0.1:
    #        f = np.arange(1e-4, 101e-5, 1e-5)
    #    elif 0.2 <= g <= 0.4:
    #        f = np.arange(1e-3, 101e-4, 1e-4)
    #    elif  0.3 <= g:
    #        f = np.arange(1e-2, 1e-1, 1e-3)
    #    else:
    #        print('error: unknown value of g')         
    else:       
        print('error: unknown value of a')       
    return f