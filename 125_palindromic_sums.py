from utils import is_palindrome
import numpy as np

m = 10**8
l = np.arange(1, int(np.sqrt(m)) + 1)
squares = l**2

palindromes = []
for start in range(len(squares)):
    print("Start at", start)
    k = 2
    rolling_sum = squares[start:start+k].sum()
    while rolling_sum < m and start+k <= len(l):
        if is_palindrome(rolling_sum):
            palindromes.append(rolling_sum)
        k += 1
        rolling_sum = squares[start:start+k].sum()

print(palindromes)
print(len(palindromes))
print(sum(palindromes))
palindromes = set(palindromes)
print(len(palindromes))
print(sum(palindromes))