class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcdM(num1, num2):
            if num1 % num2 == 0:
                return num1
            return gcd(num2, num1 % num2 )
        return gcdM(min(nums), max(nums))