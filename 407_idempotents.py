import math

limit = 100

def m(n):
    m = 0
    for a in range(n):
        if (a**2 - a) % n == 0:
            m = a
    return m

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        div = float(n) / i
        if int(div) == div:
            return False
    return True

def crible(n):
    numbers = range(2, n + 1)
    prems = []
    i = 0
    while numbers != []:
        head = numbers[0]
        prems.append(head)
        j = 1
        while head * j <= n:
            if head * j in numbers:
                numbers.remove(head * j)
            j += 1
    return prems



for i in range(10):
    m(i)
