import pulp
from pulp import * 

# declare your variables
x1 = LpVariable("x1",lowBound=0,cat='Integer')  
x2 = LpVariable("x2",lowBound=0,cat='Integer') 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += 20*x1 + 18*x2 >= 400  #first class
prob += 50*x1 + 30*x2 >= 750  #business class
prob += 110*x1 + 44*x2 >= 400  #economy class

# defines the objective function to maximize
prob += 10000*x1 + 8500*x2

# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]

# print the results x1 = 20, x2 = 60
value(x1)
value(x2)

print(prob)
print(x1.varValue)
print(x2.varValue)
