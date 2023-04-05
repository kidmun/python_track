class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primeFactor(num):
            i = 2
            prime = set([])
            while num > 1:
                flag = False
                while num % i == 0:
                    flag = True
                    num = num // i
                if flag:
                    prime.add(i)
             
                i += 1
            return prime
        ans = set([])
        for num in nums:
            primes = primeFactor(num)
            for p in list(primes):
                ans.add(p)
        return len(ans)