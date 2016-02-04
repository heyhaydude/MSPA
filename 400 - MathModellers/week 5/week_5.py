import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def nPr(n,r):
    f = math.factorial
    return f(n) / f(n-r)


print (nCr(52,3))

print (nCr(26,15)/nCr(30,15))

print( nCr(6,4) * (1/4)**4 * (3/4)**2 + nCr(6,5) * (1/4)**5 * (3/4)**1 + nCr(6,6) * (1/4)**6 * (3/4)**0)

# expected value
print( 0*nCr(3,0) * (2/7)**0 * (5/7)**3 + 1*nCr(3,1) * (2/7)**1 * (5/7)**2 + 2*nCr(3,2) * (2/7)**2 * (5/7)**1 + 3*nCr(3,3) * (2/7)**3 * (5/7)**0)
