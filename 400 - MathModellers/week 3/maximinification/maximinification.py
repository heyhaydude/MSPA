import scipy
from scipy import optimize as op
import pulp
from pulp import *

#c = [50,40,0,0]
#A = [[10000,15000,1,0], [180000,120000,0,1]]
#b = [450000, 5400000]

#res = op.linprog(c, A_ub=A, b_ub=b, bounds=(0, None),
#              options={"disp": True})
#print(res)
#print '\n'




# declare your variables
x1 = LpVariable("x1",lowBound=0,cat='Continuous')   # 0<= x1 <= 40
x2 = LpVariable("x2",lowBound=0,cat='Continuous') # 0<= x2 <= 1000
x3 = LpVariable("x3",lowBound=0,cat='Continuous') # 0<= x2 <= 1000

# defines the problem
prob = LpProblem("problem", LpMinimize)

# defines the constraints
prob += 2.5*x1+4.5*x2+5*x3 >= 54 
prob += 5*x1+3*x2+10*x3 >= 60
#prob += x1 >= 0
#prob += x2 >= 0
#prob += x3 >= 0

# defines the objective function to maximize
prob += 7*x1+8*x2+9*x3

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