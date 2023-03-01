class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if n == 0:
                return 1
            if n == 1:
              return x
            val1 = pow(x, n // 2)
            if n % 2 == 0:
                return val1 * val1
            else:
                return val1 * val1 * x
        if n < 0:
            val = pow(x, -n)
            return 1 / val
        else:
            val = pow(x, n)
            return val