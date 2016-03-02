import numpy as np
import matplotlib.pyplot as plt

areas = 0

for i in range(0,7,1):
    j = i+.5
    area = 1 * (7- j)
    areas += area

#print(areas)


points = np.array([(0,50), (3,61), (6,67), (9, 72), (12, 76), (15, 78), (18, 82), (21, 85), (24, 87), (27, 90), (30, 92)])
# get x and y vectors
x = points[:,0]
y = points[:,1]

# calculate polynomial
z = np.polyfit(x, y, 3)
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 31)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()