import pickle

def is_permutation(first, second):
    first, second = list(str(first)), list(str(second))
    if len(first) != len(second):
        return False
    for i, char in enumerate(first):
        if char not in second:
            return False
        else:
            second.remove(char)
    return True

def get_primes(n):
    try:
        with open('primes.pkl', 'rb') as file:
            primes, limit = pickle.load(file)
    except Exception as e:
        print(str(e))
    else:
        if limit >= n:
            return [p for p in primes if p <= n]
    primes = list(range(2, n+1))
    for p in primes:
        k = 2
        multiple = k * p
        while multiple <= n:
            try:
                primes.remove(multiple)
            except ValueError:
                pass
            k += 1
            multiple = k * p
    try:
        with open('primes.pkl', 'wb') as file:
            pickle.dump(file=file, obj=(primes, n))
    except Exception as e:
        print(str(e))
    else:
        print('Primes saved until', n)
    return primes

def decompose_rec(n, l, primes):
    if n <= 1:
        return l
    p = primes.pop(0)
    if n % p == 0:
        counter = 0
        while n % p == 0:
            n /= p
            counter +=1
        l += [(p, counter)]
        return decompose_rec(n, l, primes)

def decompose(n):
    return decompose_rec(n, [], get_primes(n))

def is_palindrome(n):
    s = str(n)
    begin = iter(s)
    end = reversed(s)
    for _ in range(len(s)//2):
        if next(begin) != next(end):
            return False
    return True

