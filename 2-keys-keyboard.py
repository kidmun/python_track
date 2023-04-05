class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        primes = []
        i = 2
        while i**2 <= n:
            while n % i == 0 and n > 1:
                primes.append(i)
                n = n // i
            i += 1
        if n > 1:
            primes.append(n)
        if primes:
            return sum(primes)
        return n