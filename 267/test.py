from math import *

fact = [factorial(n) for n in range(10)]

print(fact)

def f(n):
    return sum(fact[int(i)] for i in str(n))

def sumDigits(n):
    return sum(int(i) for i in str(n))

def sf(n):
    return sumDigits(f(n))

def generate(nDigits, last):
    if nDigits == 1:
        return range(last, 10)
    return [int(str(i) + str(other)) for i in range(last, 10) for other in
            generate(nDigits - 1, i)]

def launch(index):
    counter = 0
    nDigits = 1
    g = {}
    while len(g) < index:
        print("Number of digits ", nDigits)
        for i in generate(nDigits, 1):
            res = sf(i)
            if res <= index:
                if not res in g:
                    g[res] = i
                    print("New one: {:d} ({:d}) ({:d}/{:d})".format(res, i, len(g), index))
        nDigits += 1

    print(g)
    print(sum(sumDigits(i) for i in g.values()))

launch(40)

def decompose_rec(n, i):
    if i==1:
        return [n]
    return [n // fact[i]] + decompose_rec(n % fact[i], i - 1)

def decompose(n):
    k = n // fact[9]
    for j in range(k, 0, -1):
        yield [j] + decompose_rec(n - j * fact[9], 8)

def other(n):
    return int(str(n % 9) + "".join("9" for i in range(n // 9)))

for i in decompose(5999999999):
    print(i)

print(sf(int("1223334444567777888" + "".join(["9" for i in range(16534)]))))
print(other(5))
