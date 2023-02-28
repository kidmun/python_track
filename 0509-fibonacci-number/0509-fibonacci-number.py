class Solution:
    def __init__(self):
        self.count = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.count:
            return self.count[n]
        self.count[n] = self.fib(n-1) + self.fib(n-2)
        return self.count[n]
    