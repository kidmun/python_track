class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = []
        def checkPrime(num):
            if (num % 2 == 0 and num != 2) or num == 1:
                return False
            i = 3
            while i ** 2 <= num:
                if num % i == 0:
                    return False
                i += 2
            return True
        ans = []
        for i in range(left, right +1):
            if checkPrime(i):
                primes.append(i)
            if len(primes) >= 2:
                if primes[-1] - primes[-2] <= 2:
                    ans = [primes[-2], primes[-1]]
                    break
                if ans and primes[-1] - primes[-2] < (ans[1] - ans[0]):
                    print(primes[-1] - primes[-2])
                    ans = [primes[-2], primes[-1]]
                elif not ans:
                    ans =  [primes[-2], primes[-1]]
        if ans:
            return ans
        return [-1, -1]