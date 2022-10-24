import numpy as np
import scipy
from scipy.stats import norm
#Creating functions for Q, r, and B. And a solver that combines them to create a solution

def Q(B, delta, Cf, Cp, Ch): 
    tel = 2*delta*(Cf + (Cp * B))
    q = np.sqrt(tel/Ch)
    return q
               
def r(Q, delta, std, mu, Cp, Ch, I=0):
    tel = (delta * Cp) + ((I-1) * Ch * Q)
    if tel < 0:
        return 0
    nev = (delta * Cp) + (I * Ch * Q)
    r = norm.ppf(tel/nev, mu, std)
    return r
    
def B(R, std, mu):
    fir = (mu - R) * (1 - norm.cdf((R-mu)/std)) #CDF
    sec = std * norm.pdf((R-mu)/std) #PDF
    b = fir + sec
    return b

def solve(delta, std, mu, Cf, Cp, Ch, I=0):
    Ql, Rl, Bl = [], [], []
    Qi, Ri, Bi = 0, 0, 0
    for i in range(1, 11): 
        Qi = Q(Bi, delta, Cf, Cp, Ch)
        Ri = r(Qi, delta, std, mu, Cp, Ch, I)
        Bi = B(Ri, std, mu)
        Ql.append(round(Qi, 1))
        Rl.append(round(Ri, 1))
        Bl.append(round(Bi, 1))
    return Ql, Rl, Bl

#Example
print("\nBackorder: ", *solve(100, 17, 300, 500, 10, 1, 0), sep="\n") 
print("\nLost Sales: ", *solve(100, 17, 300, 500, 10, 1, 1), sep="\n")