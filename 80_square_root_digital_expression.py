from decimal import *

import math

getcontext().prec = 110
somme = 0
for i in range(101):
    if int(math.sqrt(i)) != math.sqrt(i):
        print "we do", i
        s = [int(char) for char in str(Decimal(i).sqrt()) if char != "."][:100]
        print "now, s", s
        somme += sum(s)
        print "now, somme", somme
print somme
