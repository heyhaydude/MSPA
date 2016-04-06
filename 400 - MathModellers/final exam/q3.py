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

# The first example shows how to generate and print a second degree
# polynomial with coefficients, 1, -3 and 2.  The software is not limited
# to second degree polynomials.  Higher order can be generated.  The critical
# thing is to have all the coefficients in the right sequence.

p=poly1d([(25/8.0),-250,5000])

h= p.deriv(m=1)  # First derivative with m=1.
#t= p.deriv(m=2)  # Second derivative with m=2.

print('\nEquation')
print p

print('\nEquation Roots of polynomial')
print p.roots
print('\nEquation y value of roots')
print p(p.roots)

print('\n\nDerivative')
print h
print('\nDerivative Roots of polynomial')
print h.roots
print('\nDerivative y value of roots')
print p(h.roots)

#second derivation
#print p.deriv(m=2)
#print p.deriv(m=2)(0)
#print p.deriv(m=2)(8)

#second derivative
print('\nSecond Derivative Roots of polynomial')
print p.deriv(m=2).roots
print('\nSecond Derivative y value of roots')
print p(p.deriv(m=2).roots)

x=linspace(-8,6.1,101)
y=p(x)
yd=h(x)
ydd= p.deriv(m=2)(x)

print max(p(x))

plot (x,y,label ='y=p(x)')
plot (x,yd,label ='First Derivative')
plot (x,ydd,label ='Second Derivative')
legend(loc='best')

xlabel('x-axis')
ylabel('y-axis')
title ('Plot Showing Function and First Derivative')
show()

## Exercise: Refer to Lial Section 14.1 Example 2.  Duplicate the results 
## showing plots of the function and derivatives.  Compare to the answer sheet.

#figure()
#p=poly1d([3,-4,-12,0,2])
#print ('\nFourth Degree Polynomial') 
#print p
#print ('\nFirst Derivative')
#g= p.deriv(m=1) # First derivative with m=1.
#print g
#print ('\nSecond Derivative')
#q= p.deriv(m=2) # Second derivative with m=2.
#print q
#x=linspace(-2,3,101)
#y=p(x)
#yg=g(x) # These statements define points for plotting.
#yq=q(x)
#y0=0*x # This statement defines the y axis for plotting.
#plot (x,y,label ='y=p(x)')
#plot (x,yg,label ='First Derivative')
#plot (x,yq,label ='Second Derivative')
#legend(loc='best')

#plot (x,y0)
#xlabel('x-axis')
#ylabel('y-axis')
#title ('Plot Showing Function, First and Second Derivatives')
#show()