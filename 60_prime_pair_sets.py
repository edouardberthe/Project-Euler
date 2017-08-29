from itertools import product

limit = 10**6
primes = []
not_primes = set([0, 1])

# Crible d'Erathostene : on remplit primes (en utilisant not_primes)
print "Loading of the primes until", limit
for head in range(2, limit + 1):
    if head not in not_primes:
        primes.append(head)
        i = 2
        next_not_prime = i * head
        while next_not_prime <= limit:
            not_primes.add(next_not_prime)
            i += 1
            next_not_prime = i * head
print "Primes loaded\n"


def check(prime1, prime2):
    return int(str(prime1) + str(prime2)) in primes and int(str(prime2) + str(prime1)) in primes


def check_set(prime1, l):
    for prime in l:
        if not check(prime1, prime):
            return False
    return True

print "Test check"
for i in range(10):
    for j in range(i + 1):
        print i, j, check(i, j)
print "End test check\n"

sets = []
max_len = 1
for prime in primes:
    sets.append([prime])
    for set in sets:
        if check_set(prime, set):
            set.append(prime)
            if len(set) > max_len:
                max_len = len(set)
                print "New max len :", max_len, "for", set, "whose sum is", sum(set)

print sets