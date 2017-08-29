counts = {}

def count(n, m):
    if (n, m) not in counts:
        if m > n:
            val = count(m, n)
        elif m == 0:
            val = 0
        else:
            val = count(n, m - 1) + m * n * (n+1) / 2
        counts[(n, m)] = val
    return counts[(n, m)]


print "Test count"
for i in range(1, 10):
    for j in range(1, i + 1):
        print i, j, count(i, j)
print "Fin test count"

best = 0, 0, 0

for i in range(2001):
    for j in range(2001):
        c = count(i, j)
        if abs(c - 2000000) < abs(best[0] - 2000000):
            best = c, i, j, i*j

print best