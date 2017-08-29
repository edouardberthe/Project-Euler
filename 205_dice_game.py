from itertools import product

peter, colin = {}, {}

for i in product(range(1, 7), repeat=6):
    s = sum(i)
    if s not in colin:
        colin[s] = 1
    else:
        colin[s] += 1

for i in product(range(1, 5), repeat=9):
    s = sum(i)
    if s not in peter:
        peter[s] = 1
    else:
        peter[s] += 1

print colin
print peter

wins = 0
