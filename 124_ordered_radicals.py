from math import *
from utils import get_primes
import sys
import pickle

sys.setrecursionlimit(10000)

m = 100000
k = 2

primes = get_primes(m)

def rec(prod, n, k):
    if n <= 1:
        return prod
    p = primes[k]
    if n % p == 0:
        prod *= p
        while n % p == 0:
            n /= p
    return rec(prod, n, k + 1)

def rad(n):
    return rec(1, n, 0)

try:
    with open('rad.pkl', 'rb') as file:
        rads = pickle.load(file)
except Exception:
    rads = [rad(n) for n in range(m+1)]
    try:
        with open('rad.pkl', 'wb') as file:
            pickle.dump(file=file, obj=rads)
    except Exception as e:
        print(str(e))

d = sorted(enumerate(rads), key=lambda x: x[1])
print(d[10000])