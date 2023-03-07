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

def decompose(n):
    primes = get_primes(n)
    if n <= 1:
        return {}
    d = {}
    for prime in primes:
        first = True
        while n % prime == 0:
            if first:
                d[prime] = 1
                first = False
            else:
                d[prime] += 1
            n /= prime
    return d


def is_palindrome(n):
    s = str(n)
    begin = iter(s)
    end = reversed(s)
    for _ in range(len(s)//2):
        if next(begin) != next(end):
            return False
    return True


def divisors(n):
    d = decompose(n)
    res = 1
    for prime, exp in d.items():
        res *= exp+1
    return res - 1
    