import numpy as np
import math

def optServiceInterval(MTTF, alfa, Cpm, Cu): #find tau
    fir = MTTF/(math.gamma((1+(1/alfa))))
    sec = (Cpm/(Cu*(alfa-1)))**(1/alfa)
    return fir * sec

def failureRate(MTTF, alfa, Cpm, Cu, tau): #rate of failure
    fir = (((math.gamma(1+(1/alfa)))/MTTF)**(alfa)) * tau**(alfa-1)
    sec = 1 - ((0.1*alfa*tau**2)/(MTTF**2)) + ((0.09*alfa-0.2)*tau)/MTTF
    return fir * sec 

#Example
failRate = failureRate(600, 4, 5000, 35000, optServiceInterval(600, 4, 5000, 35000))

print("Effective failure rate: ", failRate)


