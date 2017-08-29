from utils import is_permutation

cubics = dict()


def insert(i):
    cube = i**3
    for cubic in cubics:
        if is_permutation(cubic, cube):
            cubics[cubic].append(i)
            if len(cubics[cubic]) == 5:
                return cubic, cubics[cubic]
    cubics[cube] = [i]
    return False

i = 1
res = insert(i)
while not res:
    i += 1
    res = insert(i)
    if i % 100 == 0:
        print i, i**3

print res

