class Solution:
    def minSteps(self, n: int) -> int:
        # primes = []
        # i = 2
        # while i**2 <= n:
        #     while n % i == 0 and n > 1:
        #         primes.append(i)
        #         n = n // i
        #     i += 1
        # if n > 1:
        #     primes.append(n)
        # return sum(primes)
        dp = [0] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            x = i - 1
            while i % x != 0:
                x -= 1
            dp[i] = dp[x] + i // x
        return dp[n]