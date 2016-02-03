import pulp
from pulp import * 

# declare your variables
x1 = LpVariable("x1",lowBound=0,cat='Integer')  
x2 = LpVariable("x2",lowBound=0,cat='Integer') 
x3 = LpVariable("x3",lowBound=0,cat='Integer') 

# defines the problem
prob = LpProblem("problem", LpMaximize)

# defines the constraints
prob += x1 + x2 <= 10   #no more than 10 classical and jazz
prob += x3 <= 8         #no more than 8 rock
prob += x3 - 2*x1 == 0

# defines the objective function to maximize
# attendance function
prob += 700*x1 + 800*x2 + 300*x3

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

print('\n\nattendance is %f'%(700*x1.varValue + 800*x2.varValue + 300*x3.varValue))

