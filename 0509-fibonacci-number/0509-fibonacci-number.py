class Solution:
    def fib(self, n: int) -> int:
        count = {0:0, 1:1}
        if n in count:
            return count[n]
        val1 = self.fib(n-1)
        if n not in count:
            count[n] = val1
        return val1 + self.fib(n-2)
    