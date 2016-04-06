# MSPA 400 Session 7 Python Module #2.

# Reading assignment:
# "Think Python" 2nd Edition Chapter 8 (8.3-8.11)
# "Think Python" 3td Editon (pages 85-93)

# Module #2 objective:  demonstrate some of the unique capabilities of numpy 
# and scipy.  (Using the poly1d software from numpy, it is possible to 
# differentiate, # integrate, and find the roots of polynomials.  Plotting the
# results illustrates the connection between the different functions.)

import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import poly1d, linspace
import scipy.stats
from scipy.stats import norm


def inte(x):
    return (2.5*x**2 + (10.0/3.0)*x**(3.0/2.0))/135.0

def inte1(x):
    return (5*x + 10.0*x**.5)/135.0

def vare(x):
    return ((5.0/3.0)*x**3 + (10.0/5.0)*x**(5.0/2.0))/135

def vare2(a,b):
    return ((vare(a) - vare(b)) - (inte(a) - inte(b))**2)

def std2(a,b):
    return numpy.sqrt(vare2(a,b))

print inte(25) - inte(4)
print vare2(25,4)
print std2(25,4)
print inte1(25) - inte1(14.17)

#p1=poly1d([1,0])
#p2=poly1d([1,1])
#p3=p1*p2  
#print p3.integ()

#h= p.deriv(m=1)  # First derivative with m=1.
##t= p.deriv(m=2)  # Second derivative with m=2.

#print('\nEquation')
#print p

#print('\nEquation Roots of polynomial')
#print p.roots
#print('\nEquation y value of roots')
#print p(p.roots)

#print('\n\nDerivative')
#print h
#print('\nDerivative Roots of polynomial')
#print h.roots
#print('\nDerivative y value of roots')
#print p(h.roots)

##second derivation
##print p.deriv(m=2)
##print p.deriv(m=2)(0)
##print p.deriv(m=2)(8)

##second derivative
#print('\nSecond Derivative Roots of polynomial')
#print p.deriv(m=2).roots
#print('\nSecond Derivative y value of roots')
#print p(p.deriv(m=2).roots)

#x=linspace(-8,6.1,101)
#y=p(x)
#yd=h(x)
#ydd= p.deriv(m=2)(x)

#print max(p(x))

#plot (x,y,label ='y=p(x)')
#plot (x,yd,label ='First Derivative')
#plot (x,ydd,label ='Second Derivative')
#legend(loc='best')

#xlabel('x-axis')
#ylabel('y-axis')
#title ('Plot Showing Function and First Derivative')
#show()
