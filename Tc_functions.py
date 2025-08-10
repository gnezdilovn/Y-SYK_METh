import numpy as np
from numpy.linalg import eig
from scipy import special
from scipy.special import zeta, polygamma, factorial, psi

# w -- fermionic Matsubara frequencies in units of temperature T,
# o -- bosonic Matsubara frequencies in units of temperature T,
# T -- temperature/Fermi energy,
# a -- Debye frequency/Fermi energy,
# g -- unitless electron-boson coupling constant,
# N2 -- number of Matsubara frequencies in the positive frequency domain.   

# exact determinant for Tc from the linearized gap equation
def Zp(N2, T, g, a):
    n = np.arange(0, N2, 1)
    dim = len(n)
    w = np.pi * (2 * n + 1) 
    f = np.zeros(dim)
    for i in range(dim):
        o = 2 * np.pi * np.arange(1, n[i] + 1, 1)
        log_t = np.log(o ** 2 * (T / a) ** 2 + 2. * g * np.pi * o * T + 1.)
        log_b = np.log(o ** 2 * (T / a) ** 2 + 2. * g * np.pi * o * T)
        f[i] = 1. + 2. * g * np.pi * np.sum(log_t - log_b) / w[i]
    return w, f    

def Det(N2, T, g, a):
    n = np.arange(0, N2, 1)
    dim = len(n)
    dim2 = (dim, dim)
    w = np.pi * (2 * n + 1)
    Mat = np.zeros(dim2)
    Z = Zp(N2, T, g, a)[1]
    for i in range(dim):
        for j in range(dim):
            W = np.abs(w[i] + w[j])
            log_t_plus = np.log(W ** 2 * (T / a) ** 2 + 2. * g * np.pi * W * T + 1.)
            log_b_plus = np.log(W ** 2 * (T / a) ** 2 + 2. * g * np.pi * W * T)
            if j == i:
                Mat[i][j] = g * np.pi * (log_t_plus - log_b_plus) / np.abs(w[j]) / Z[i] - 1. 
            else:
                dw = np.abs(w[i] - w[j])
                log_t_minus = np.log(dw ** 2 * (T / a) ** 2 + 2. * g * np.pi * dw * T + 1.)
                log_b_minus = np.log(dw ** 2 * (T / a) ** 2 + 2. * g * np.pi * dw * T)
                Mat[i][j] = g * np.pi * (log_t_minus - log_b_minus + log_t_plus - log_b_plus) / np.abs(w[j]) / Z[i] 
    D = np.linalg.det(Mat)        
    return D 

def eigensystem(N2, T, g, a):
    n = np.arange(0, N2, 1)
    dim = len(n)
    dim2 = (dim, dim)
    w = np.pi * (2 * n + 1)
    Mat = np.zeros(dim2)
    Z = Zp(N2, T, g, a)[1]
    for i in range(dim):
        for j in range(dim):
            W = np.abs(w[i] + w[j])
            log_t_plus = np.log(W ** 2 * (T / a) ** 2 + 2. * g * np.pi * W * T + 1.)
            log_b_plus = np.log(W ** 2 * (T / a) ** 2 + 2. * g * np.pi * W * T)
            if j == i:
                Mat[i][j] = g * np.pi * (log_t_plus - log_b_plus) / np.abs(w[j]) / Z[i] 
            else:
                dw = np.abs(w[i] - w[j])
                log_t_minus = np.log(dw ** 2 * (T / a) ** 2 + 2. * g * np.pi * dw * T + 1.)
                log_b_minus = np.log(dw ** 2 * (T / a) ** 2 + 2. * g * np.pi * dw * T)
                Mat[i][j] = g * np.pi * (log_t_minus - log_b_minus + log_t_plus - log_b_plus) / np.abs(w[j]) / Z[i] 
    es, vs = eig(Mat)
    fs = np.transpose(vs)        
    return w, es, fs 

def delta_0(N2, T_array, g, a):
    d0 = np.zeros(len(T_array))
    for t in range(0, len(T_array)):
        d0[t] = eigensystem(N2, T_array[t], g, a)[2][0][0]
    return np.abs(d0)    

def ansatz(N2, T, B):
    n = np.arange(0, N2, 1)
    w = np.pi * (2 * n + 1)
    norm = 4. * np.sqrt(B) * T / np.tanh(0.5 / T / np.sqrt(B))
    f = norm / (1. + B * T ** 2 * w ** 2)
    return f    
    
# determinant for Tc from the linearized gap equation in strong coupling regime
def Zp_sc(N2, T):
    n = np.arange(0, N2, 1)
    dim = len(n)
    w = np.pi * (2 * n + 1) 
    f = np.zeros(dim)
    for i in range(dim):
        o = 2 * np.pi * np.arange(1, n[i] + 1, 1)
        fun = 1. / (2. * o * T)
        f[i] = 1. + 2. * np.sum(fun) / w[i]
    return w, f   

def Det_sc(N2, T):
    n = np.arange(0, N2, 1)
    dim = len(n)
    dim2 = (dim, dim)
    w = np.pi * (2 * n + 1)
    Mat = np.zeros(dim2)
    Z = Zp_sc(N2, T)[1]
    for i in range(dim):
        for j in range(dim):
            W = np.abs(w[i] + w[j])
            f_plus = 1. / (2. * W * T)
            if j == i:
                Mat[i][j] = f_plus / np.abs(w[j]) / Z[i] - 1.
            else:
                dw = np.abs(w[i] - w[j])
                f_minus = 1. / (2. * dw * T)
                Mat[i][j] = (f_minus + f_plus) / np.abs(w[j]) / Z[i]
    D = np.linalg.det(Mat)        
    return D 

# T in units of boson mass
# exact determinant for Tc from the linearized gap equation for the Allen-Dynes case
def Zp_AD(N2, T, g):
    n = np.arange(0, N2, 1)
    #dim = len(n)
    w = np.pi * (2 * n + 1) 
    #f = np.zeros(dim)
    #for i in range(dim):
    X = np.imag(psi(1. + 1j / (2. * np.pi * T)) - psi(0.5 + (T * w + 1j) / (2. * np.pi * T)))
    f = 1. + g * X / w / T
    return w, f    

def Det_AD(N2, T, g):
    n = np.arange(0, N2, 1)
    dim = len(n)
    dim2 = (dim, dim)
    w = np.pi * (2 * n + 1)
    Mat = np.zeros(dim2)
    Z = Zp_AD(N2, T, g)[1]
    for i in range(dim):
        for j in range(dim):
            dw2 = T ** 2 * (w[i] - w[j]) ** 2
            W2 = T ** 2 * (w[i] + w[j]) ** 2
            L_plus =  1. / (W2 + 1.)
            L_minus = 1. / (dw2 + 1.)
            if j == i:
                Mat[i][j] = g * np.pi * L_plus / w[j] / Z[i] - 1. 
            else:
                Mat[i][j] = g * np.pi * (L_plus + L_minus) / w[j] / Z[i] 
    D = np.linalg.det(Mat)        
    return D 