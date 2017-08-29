def reverse(i):
    return int(str(i)[::-1])

def is_palindrome(n):
    return n == reverse(n)

def search(i):
    rec = 0
    while rec < 50:
        i += reverse(i)
        if is_palindrome(i):
            return False
        rec += 1
    return True

print sum([1 for i in range(1, 10001) if search(i)])
