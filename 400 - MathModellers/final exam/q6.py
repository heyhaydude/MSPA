import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import linspace

# generate line values
x= linspace(-10,6,1000)
# function
y= -1/(x+2)**2 + 4
# first derivative
yprime= 2*(x+2)**-3
# secon derivative
yprimeprime = -6*(x+2)**-4

figure()  
ylim(-10,10)
plot (x,y)

legend (('function','x'),loc=2)

show()