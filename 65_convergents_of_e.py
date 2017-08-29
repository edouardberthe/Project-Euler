import numpy as np
from fractions import Fraction

a = np.matrix([[1, 2], [1, 1]])

u = np.array([[1], [1]])
for i in range(10):
    u = a * u
    print u


def rec(n, i):
    if i == 0:
        val = 2
    elif i % 3 == 2:
        val = 2 * (i // 3 + 1)
    else:
        val = 1
    if i == n:
        return val
    else:
        return val + Fraction(1, rec(n, i+1))


def frac_exp(n):
    return rec(n - 1, 0)

for i in range(1, 10):
    print frac_exp(i)

f = frac_exp(100)
print f
print f.numerator
print sum((int(char) for char in str(f.numerator)))
