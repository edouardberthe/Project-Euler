import numpy.polynomial.polynomial as poly

def lagrange(k,n):
    p = poly.Polynomial([1])
    for i in range(1, n+1):
        if i != k:
            p = p*poly.Polynomial([-i,1]) / (k-i)
    return p

def interp(l):
    p = poly.Polynomial([0])
    for i, elem in enumerate(l):
        p += lagrange(i+1, len(l)) * elem
    return p

def OP(poly, i):
    return interp([poly(j) for j in range(1, i+1)])

def diff(p,q):
    for i in range(1, 100):
        if abs(p(i) - q(i)) > 1:
            return q(i)
    return False

v = poly.Polynomial([0, 0, 0, 1])

u = poly.Polynomial([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])

sum([int(diff(u, OP(u,i))+0.1) for i in range(1,12)])