init = 'ABCDEF'

pile = [init]

def permut(string, index):
    return string[:index] + string[index:][::-1]

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def previous(string):
    for index, char in enumerate(string):
        if char != init[index]: 
            if string[-1] != init[index]:
                return [permut(string, index - 1)]
            elif index + 1 < len(string) - 1:
                return [permut(string, j) for j in range(index + 1, len(string) - 1)]
            else:
                return [permut(string, len(string) - 3)]
    return [permut(string, len(string) - 2)]

for i in range(10):
    print pile
    pile = [p for p in previous(string) for string in pile]

print pile