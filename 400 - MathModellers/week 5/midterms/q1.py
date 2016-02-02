import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import linspace

# generate line values
x= linspace(0,2000,1000)
# cost equation
y= 2811.60 + 1 * x
# income equation
z= 2.8 * x

figure()  
plot (x,y)
plot (x,z)
# intersection point x=1562 and y=4373.6
plot ([1562],[4373.6],'ro')

legend (('cost','revenue'),loc=2)
title ('Breakeven Analysis')
show()