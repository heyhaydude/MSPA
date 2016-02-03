import pulp
from pulp import * 

# declare your variables
x1 = LpVariable("x1",lowBound=0,cat='Integer')  
x2 = LpVariable("x2",lowBound=0,cat='Integer') 
x3 = LpVariable("x3",lowBound=0,cat='Integer') 

# defines the problem
prob = LpProblem("problem", LpMaximize)

# defines the constraints
prob += x1 + x2 + x3 <= 99  #less than 100 pages
prob += x3 - x2 >= 5  #environ. at least 5 more than military
prob += x1 - x2 >= 5  #economy at least 5 more than military
#prob += x2 >= 3

# defines the objective function to maximize
# impact function
prob += 5*x1
prob += 2*x2
prob += 4*x3

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

