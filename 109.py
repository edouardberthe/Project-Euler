from itertools import combinations_with_replacement

simples = range(1, 21) + [25]
doubles = [2*x for x in range(1, 21)] + [50]
triples = [3*x for x in range(1, 21)]

count = 0
for first in simples + doubles + triples:
    for second in simples + doubles + triples:
        for third in doubles:
            count += 1
print count

fact_array = {0:1}

def fact(n):
    if n not in fact_array:
        fact_array[n] = n * fact(n-1)
    return fact_array[n]

def binom(k,n):
    return fact(n) / (fact(n-k) * fact(k))

print len(doubles) + len(simples + doubles + triples) * len(doubles) + len([i for i in combinations_with_replacement(simples + doubles + triples, 2)]) * len(doubles)

count = 0
number = 0

for first in doubles:
    number += 1
    if first < 100:
        count += 1

for first in simples + doubles + triples:
    for second in doubles:
        number += 1
        if first + second < 100:
            count += 1

for first, second in combinations_with_replacement(simples + doubles + triples, 2):
    for third in doubles:
        number += 1
        if first + second + third < 100:
            count += 1

print number
print count