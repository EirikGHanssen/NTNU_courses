import numpy as np

def generateAMatrix(mu, lam, N, k=1, C=np.inf):
    A = np.zeros([N, N])
    for i in range(0, N-1): # lambda values below diagonal
        A[i][i+1] = lam
        if (k==2) and (i>0): #if k != 1, then increase lamda values up to k
            A[i][i+1] = (A[i][i+1])*k
    for i in range(1, N):    #mu values above diagonal
        if (i <= C):       #Makes sure that for MMCN queues that we have max C servers
            A[i][i-1] = mu * (i)
        else:
            A[i][i-1] = mu * C 
    for i in range(0, N):
        s = 0   
        for j in range(0, N):
            if i != j: 
                s = s + A[i][j]
        A[i][i] =- s  
    return A

def steadyState(A, N): #Creating steady state solutions from matrix A
    Anew = np.copy(A)
    for i in range(0, N):
        Anew[i][0] = 1
    B = np.zeros([N])    
    B[0] = 1
    P = np.linalg.solve(np.transpose(Anew), B)
    return P

def timeDepend(A, N, maxTime=50, dt = 0.1): #Creating time dependant solutions from matrix A
    Anew = np.copy(A)
    P = np.zeros([N])  
    P[0] = 1 
    IM = np.eye(N) + np.dot(Anew, dt) #Eye is Identity matrix
    for t in np.arange(0, maxTime, dt): 
        P = np.dot(P, IM)
    return P

def analytical_sol(C, N, rho):  #Analytical solution for M/M/C=N/N=C queues
    teller = []
    nevner = 0
    for j in range(0, C+1):
        teller.append((rho**j)/np.math.factorial(j))
        nevner += (rho**j)/(np.math.factorial(j))
    for i in range(len(teller)):
        teller[i] = teller[i]/nevner
    return teller

#Examlpe: 
A = generateAMatrix(0.01, 0.2, 4, 1) 
print(A)
print(f"Steady state solution: \n {steadyState(A, 4)}") 
print(f"Time dependant state solution: 8hours-workday\n{timeDepend(A, 4, 8, 0.1)}")