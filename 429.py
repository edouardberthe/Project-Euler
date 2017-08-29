limit = 10**3
primes = []
not_primes = set([0, 1])

# Crible d'Erathostene : on remplit primes (en utilisant not_primes)
for head in range(2, limit + 1):
    if head not in not_primes:
        primes.append(head)
        i = 2
        next_not_prime = i * head
        print len(primes), len(not_primes), primes[-1]
        while next_not_prime <= limit:
            not_primes.add(next_not_prime)
            i += 1
            next_not_prime = i * head

print "TERMINE"

print "Test primes"
for i in range(20):
    print i, i in primes
print "Fin test\n"

def val(n, p):
    res = 0
    if n < 2:
        return 0, n
    if p < 2:
        raise ValueError("n < 2 or p < 2")
    while n % p == 0:
        res += 1
        n = n / p
    return res, n

print "Test val(n,p)"
for i in range(2, 20):
    print i
    for j in range(2, i):
        if j in primes:
            print "\tval", j, "addique :", val(i,j)[0], val(i,j)[1]
    print "\n"
print "Fin test\n"

def decompose(n):
    res = {}
    for i in range(2, n + 1):
        if i in primes:
            v, new = val(n, i)
            if v > 0:
                res[i] = v
                n = new
    return res

print "Test decompose"
for i in range(20):
    print i, decompose(i)

print decompose(limit)
print "Fin test\n"

def insert(first, second, prime, valuation):
    if prime in first:
        first[prime] += valuation
        return [(first, second)]
    elif prime in second:
        second[prime] += valuation
        return [(first, second)]
    else:
        first_copy = first.copy()
        second_copy = second.copy()
        first[prime] = valuation
        second_copy[prime] = valuation
        return [(first, second), (first_copy, second_copy)]

print "Test insert"
for prime, valuation in decompose(5).iteritems():
    print "\t\t{", prime, ":", valuation, "} :", insert(decompose(3), decompose(8), prime, valuation)

def s(n):
    if n == 4:
        return [({1:1}, decompose(24)), (decompose(3), decompose(8))]
    res = []
    decomposition = decompose(n)
    for first, second in s(n-1):
        for new_prime, new_val in decomposition.iteritems(): 
            for new in insert(first, second, new_prime, new_val):
                if new not in res:
                    res.append(new)
    return res

print "Test s(n)"
print s(6)
