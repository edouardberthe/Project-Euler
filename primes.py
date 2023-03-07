import sys
import math

class PrimeGenerator:
    
    def __init__(self):
        self.until = 2
        self.primes = set()
        self.dico = {}
    
    def is_prime(self, n: int) -> bool:
        if n > self.until:
            self.compute_until(n)
        return n in self.primes
    
    def primes_until(self, n: int):
        if n > self.until:
            self.compute_until(n)
        return self.primes

    def compute_until(self, until: int):
        if until < self.until:
            pass
        i = self.until
        while i <= until:
            if i in self.dico:
                for p in self.dico[i]:
                    tmp = p+i
                    if tmp not in self.dico:
                        self.dico[tmp] = [p]
                    else:
                        self.dico[tmp].append(p)
                del self.dico[i]
            else:
                self.primes.add(i)
                tmp = 2*i
                if tmp not in self.dico:
                    self.dico[tmp] = [i]
                else:
                    self.dico[tmp].append(i)
            i += 1
        self.until = until
    
    def decompose(self, n: int):
        if n > self.until:
            self.compute_until(n)
        ans = []
        for i in self.primes:
            curr = 0
            while n % i == 0:
                curr += 1
                n = n // i
            if curr > 0:
                ans.append((i, curr))
            if n == 1:
                break
        return ans
    
    def __iter__(self):
        for p in self.primes:
            yield p
        i = self.n
        while True:
            if is_prime(i):
                yield i
            i += 1
