import urllib2
import numpy as np

html = urllib2.urlopen('https://projecteuler.net/project/resources/p107_network.txt').read()

m = np.array([[(string, 0) for string in row.split(',')] for row in html.split()])
n = np.array([
    ['-', '16', '12', '21', '-', '-', '-'],
    ['16', '-', '-', '17', '20', '-', '-'],
    ['12', '-', '-', '28', '-', '31', '-'],
    ['21', '17', '28', '-', '18', '19', '23'],
    ['-', '20', '-', '18', '-', '-', '11'],
    ['-', '-', '31', '19', '-', '-', '27'],
    ['-', '-', '-', '23', '11', '27', '-']])
n = np.array([[(string, 0) for string in row] for row in n])

def mmax(matrix):
    m = 0
    m_i = 0
    m_j = 0
    for i in range(matrix.shape[0]):
        for j in range(i):
            if int(matrix[i,j,1]) == 0:
                try:
                    value = int(matrix[i,j,0])
                except ValueError:
                    pass
                else:
                    if value > m:
                        m = value
                        m_i = i
                        m_j = j
    return m, m_i, m_j

def msum(matrix):
    m = 0
    for i in range(matrix.shape[0]):
        for j in range(i):
            try:
                m += int(matrix[i,j][0])
            except ValueError:
                pass
    return m

def succ(matrix, k):
    ans = []
    for i in range(matrix.shape[0]):
        try:
            value = int(matrix[k,i,0])
        except ValueError:
            pass
        else:
            ans.append(i)
    return ans

for i in range(n.shape[0]):
    print succ(n, i)

def test(matrix):
    left = [0]
    checked = set([])
    while len(left) > 0:
        head = left[0]
        left = left[1:]
        for successor in succ(matrix, head):
            if successor not in checked:
                left.append(successor)
        checked.add(head)
    return checked == set(range(matrix.shape[0]))

def reduce(matrix):
    initial_sum = msum(matrix)
    while mmax(matrix) != (0,0,0):
        temp = matrix.copy()
        t, i, j = mmax(temp)
        temp[i,j] = ('-', 0)
        temp[j,i] = ('-', 0)
        if test(temp):
            print "ca marche on enleve ", t, " a ", i, j, " et ", j, i
            matrix = temp.copy()
            matrix = temp.copy()
        else:
            matrix[i,j,1] = 1
            matrix[j,i,1] = 1
        print msum(matrix)
    print "Gain de ", initial_sum - msum(matrix)

print mmax(n)
print msum(n)
reduce(n)
reduce(m)