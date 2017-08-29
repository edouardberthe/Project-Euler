def is_pandigital(n):
    s = str(n)
    for it in (iter(reversed(s)), iter(s)):
        mem = []
        for i in range(9):
            try:
                digit = next(it)
            except StopIteration:
                return False
            else:
                if digit == '0' or digit in mem:
                    return False
                mem.append(digit)
    return True

fibo = [1, 1]
for i in range(2, 500000):
    fibo.append(fibo[i-1] + fibo[i-2])

print("Fibo computed")

for i,f in enumerate(fibo):
    if i % 1000 == 0:
        print(i)
    if is_pandigital(f):
        print(i, f)
        break

print(fibo[540])
print(is_pandigital(fibo[540]))