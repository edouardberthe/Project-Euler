import math


# We can demonstrate that the number of block for the nth layer (n > 0) of a x * y * z initial block is : 
# f(n, x, y, z) = 2(xy + xz + yz) + 4(n - 1)(x + y + z) + 4(n-1)(n-2)
# So, by noting s = x + y + z and d = xy + xz + yz we obtain :
# f(n, s, d) = 4n^2 + 4(s-3)n + 2(d - 2s + 4) which is a 2nd degree polynom.
# We want f(n, s, d) = m. It has solution if delta' >= 0, thus :
# s^2 - 2s + 1 - 2d + m > 0. Then, n1 < 0 (impossible) and n2 = (-(s-3) + sqrt(delta)) / 2. We then just have to check
# if n2 is an integer.

def f(n, s, d):
    if n == 0:
        return 2 * d
    else:
        return 2 * d + 4 * (n-1) * s + 4 * (n-1) * (n-2)

def test():
    m = 1
    counts = []
    while True:
        counts = []
        for x in range(1, m):
            for y in range(x, int(m / (2*x)) + 1):
                for z in range(y, int((m/2 + x*y)/(x + y)) + 1):
                    s = x + y + z
                    d = x*y + y*z + x*z
                    delta = s**2 - 2*s + 1 - 2*d + m
                    if delta >= 0:
                        n2 = (math.sqrt(delta) - s + 3) / 2
                        if int(n2) == n2 and n2 >= 1:
                            counts.append((n2,x,y,z))
        if len(counts) == 1000:
            print "TROUVE", m, counts
            return True
        else:
            if m % 100 == 0:
                print m, " : ", len(counts)
        m += 1
test()