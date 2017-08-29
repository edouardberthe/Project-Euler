import numpy as np
import urllib2

html = urllib2.urlopen('https://projecteuler.net/project/resources/p102_triangles.txt').read()

triangles = [[int(coord) for coord in line.split(',')] for line in html.split("\n")[:-1]]

counts = 0
for triangle in triangles:
    xa, ya, xb, yb, xc, yc = triangle[0], triangle[1], triangle[2], triangle[3], triangle[4], triangle[5]
    A = np.matrix([[xc - xa, xc - xb], [yc - ya, yc - yb]])
    B = np.matrix([[xc], [yc]])
    res = A.I * B
    if res[0, 0] > 0 and res[1, 0] > 0 and 1 - res[0, 0] - res[1, 0] > 0:
        counts += 1

print counts
