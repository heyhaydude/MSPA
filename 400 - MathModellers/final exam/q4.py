import pulp
from pulp import * 

# declare your variables
x1 = LpVariable("x1",lowBound=0,cat='Integer')  
x2 = LpVariable("x2",lowBound=0,cat='Integer') 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += .3*x1 + .06*x2 >= 350  #white reams
prob += 10*x1 + 10*x2 + 20*x3 >= 400  #yellow reams

# defines the objective function to minimize
prob += .3*x1 + .06*x2

# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]

# print the results x1 = 20, x2 = 60
value(x1)
value(x2)
value(x3)

print(prob)
print(x1.varValue)
print(x2.varValue)
print(x3.varValue)

print(x1.varValue * 60 + x2.varValue * 40 + x3.varValue * 50)
