from fractions import Fraction

valids2 = set()
for d in range(8, -1, -1):
    print "d :", d, ", len(valids2) :", len(valids2)
    for n in range(int(d / 3. + 1), int(d / 2. + 1)):
        valids2.add(Fraction(n, d))

print len(valids2)
