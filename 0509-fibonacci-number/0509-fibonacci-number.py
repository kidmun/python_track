class Solution:
    def __init__(self):
        self.c = 2
        self.count = {0:0, 1:1}
    def fib(self, n: int) -> int:
   
        if n in self.count:
            return self.count[n]
        val1 = self.fib(n-1)
        val2 = self.fib(n-2)
        self.count[self.c] = val1 + val2
        self.c += 1
        return val1 + val2
    