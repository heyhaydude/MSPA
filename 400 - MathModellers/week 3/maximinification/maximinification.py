import pulp
from pulp import * 

# declare your variables
x1 = LpVariable("x1",lowBound=0,cat='Integer')  
x2 = LpVariable("x2",lowBound=0,cat='Integer') 
x3 = LpVariable("x3",lowBound=0,cat='Integer') 
x4 = LpVariable("x4",lowBound=0,cat='Integer') 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += 0.5*x1+38*x2+8*x3+4.2*x4 >= 277  #protein
prob += 25*x1+0*x2+39*x3+10*x4 >= 462    #carbs
prob += .3*x1+19*x2+4*x3+.5*x4 >= 91     #fat
prob += .065*x1+.4*x2+.2*x3+.2*x4 >= 1.5 #vitamin b6
prob += 13*x1+0*x2+0*x3+198*x4 >= 110    #vitamin c

# defines the objective function to maximize
prob += .77*x1+2.22*x2+.65*x3+.75*x4

# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]

# print the results x1 = 20, x2 = 60
value(x1)
value(x2)
value(x3)
value(x4)

print(prob)
print(x1.varValue)
print(x2.varValue)
print(x3.varValue)
print(x4.varValue)