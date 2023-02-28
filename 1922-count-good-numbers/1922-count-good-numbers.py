class Solution:
    def countGoodNumbers(self, n: int) -> int:
        c = ceil(n / 2)
        x =  n//2
        return (pow(5, c,10**9 + 7 ) * pow(4, x, 10**9 + 7 )) % (10**9 + 7 )