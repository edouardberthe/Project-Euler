import math

limit = 50*10**6
primes = []
not_primes = set([0, 1])

# Crible d'Erathostene : on remplit primes (en utilisant not_primes)
print "Loading of the primes until", limit
for head in range(2, int(math.sqrt(limit)) + 1):
    if head not in not_primes:
        primes.append(head)
        i = 2
        next_not_prime = i * head
        while next_not_prime <= limit:
            not_primes.add(next_not_prime)
            i += 1
            next_not_prime = i * head
print "Primes loaded\n"

sums = set()
count = 0
for a in range(int(math.sqrt(limit)) + 1):
    if a in primes:
        count += 1
        if count % 1000 == 0:
            print a
        a2 = a**2
        for b in range(int(math.pow(limit - a2, 1./3)) + 1):
            if b in primes:
                b3 = b**3
                for c in range(int(math.pow(limit - a2 - b3, 1./4)) + 1):
                    if c in primes:
                        sums.add(a2 + b3 + c**4)
print len(sums), list(sums)[-10:]
print len([i for i in sums if i <= limit])
