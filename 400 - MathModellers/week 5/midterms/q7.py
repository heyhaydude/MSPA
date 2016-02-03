import pulp
from pulp import * 

# declare your variables
x1 = LpVariable("x1",lowBound=0,cat='Continuous')  
x2 = LpVariable("x2",lowBound=0,cat='Continuous') 
x3 = LpVariable("x3",lowBound=0,cat='Continuous') 

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += 2.5*x1 + 4.5*x2 + 5*x3 >= 54  #at least 54 vitamin units
prob += 5*x1 + 3*x2 + 10*x3 >= 60  #at least 54 vitamin units

# defines the objective function to maximize
# impact function
prob += .07*x1 + .08*x2 + .1*x3

# solve the problem
status = prob.solve(GLPK(msg=0))
LpStatus[status]

value(x1)
value(x2)
value(x3)

print(prob)
print(x1.varValue)
print(x2.varValue)
print(x3.varValue)

print('\n\ncost is %f'%(.07*x1.varValue + .08*x2.varValue + .1*x3.varValue))

