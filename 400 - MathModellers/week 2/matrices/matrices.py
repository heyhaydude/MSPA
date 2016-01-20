import numpy 
from numpy import *
from numpy.linalg import *

rhs= [970,470,535]
rhs=matrix(rhs)
rhs=transpose(rhs)
print ('\nRight Hand Side of Equation')
print rhs

A =[[3,3,2],[2,1,1],[1,2,2]]
A= matrix(A)
print ('\nMatrix A')
print A

# Find inverse of A.
print ('\nInverse of A')
IA= inv(A)
print IA

# In what follows, I am converting matrices with floating point numbers  to
# matrices with integer numbers.  This is optional and being done to show
# that it is possible to do so with numpy matrices.

# Note that the function dot() performs matrix multiplication.
# Verify inverse by multiplying matrix A and its inverse IA.

print ('\nIdentity Matrix')
I= dot(A,IA)          # This converts floating point to integer.
print I

# Solve the system of equations and convert to integer values.
# With numpy it is necessary to use dot() for the product.

print '\nResults'
result = dot(IA,rhs)
print result
print '\n'


#m=matrix([[2.67,4.48,6.35,9.02],[1.76,2.82,4.59,6.91],[.94,.71,.66,.56]])
#f=matrix([[1.46,1.69,1.87,3.32],[1.25,1.47,2.78,2.36],[.44,.35,.27,.46]])

#print '\n'
#print m
#print f
#print(m-f)

a= matrix([[80,60,140],[60,30,150]])
b= matrix([[.5,.2],[.25,.2],[.25,.6]])
print(dot(a,b))
print(dot(b,a))

print (inv(matrix([[6,4],[4,7]])))


a= matrix([[27,9,27]])
a= matrix.transpose(a)
b= matrix([[2,4,6],[-1,-4,-3],[0,1,-1]])
print(dot(b,a))

print '\n'
a= matrix([[264,-182,-2]])
a= matrix.transpose(a)
b= matrix([[2,4,6],[-1,-4,-3],[0,1,-1]])
ib = inv(b)
print(dot(ib,a))