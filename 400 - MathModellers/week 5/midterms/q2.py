import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import linspace

# generate line values
t = linspace(0,50,100)
t1 = 3*t
t2 = t
t3 = 120 - 8.0/3.0*t
t4 = 60 - 4.0/3.0*t

figure()  
plot (t,t1)
plot (t,t2)
plot (t,t3)
plot (t,t4)
ylim(ymin=0)
xlim(xmax=45)

legend (('t1','t2','t3','t4'),loc='best')
title ('Possible number of people on each of 4 teams')
show()
