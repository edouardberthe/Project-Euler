from primes import PrimeGenerator

def R(k):
    return int("".join("1" for _ in range(k)))

gen = PrimeGenerator()
print(gen.primes_until(100))

print(gen.decompose(R(2)))
print(gen.decompose(R(4)))
print(gen.decompose(R(5)))
print(gen.decompose(R(8)))


