from itertools import product

functions = dict(triangle=lambda n: n * (n+1) / 2,
                 square=lambda n: n**2,
                 pentagonal=lambda n: n * (3*n - 1) / 2,
                 hexagonal=lambda n: n * (2*n - 1),
                 heptagonal=lambda n: n * (5*n - 3) / 2,
                 octagonal=lambda n: n*(3*n-2))


def follow(n1, n2):
    return str(n1)[-2:] == str(n2)[:2]

lists = {name: dict() for name in functions}
for name, function in functions.iteritems():
    n, calc = 0, function(0)
    while calc < 10000:
        if calc >= 1000:
            lists[name][n] = calc
        n += 1
        calc = function(n)
print lists
for n1, calc1 in lists['triangle'].iteritems():
    print calc1
    for n2, calc2 in lists['square'].iteritems():
        if n2 != n1 and follow(calc1, calc2):
            print "\t", calc2
            for n3, calc3 in lists['pentagonal'].iteritems():
                if n3 not in [n1, n2] and follow(calc2, calc3):
                    print "\t\t", calc3
                    for n4, calc4 in lists['hexagonal'].iteritems():
                        if n4 not in [n1, n2, n3] and follow(calc3, calc4):
                            print "\t\t\t", calc4
                            for n5, calc5 in lists['heptagonal'].iteritems():
                                if n5 not in [n1, n2, n3, n4] and follow(calc4, calc5):
                                    print "\t\t\t\t", calc5
                                    for n6, calc6 in lists['octagonal'].iteritems():
                                        if n6 not in [n1, n2, n3, n4, n5] and follow(calc5, calc6) and follow(calc6, calc1):
                                            print "\t\t\t\t\t", calc6
                                            print "Done :", n1, calc1, n2, calc2, n3, calc3, n4, calc4, n5, calc5, n6, calc6, sum([calc1, calc2, calc3, calc4, calc5, calc6])
                                            break