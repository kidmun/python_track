class Solution:
    def tribonacci(self, n: int) -> int:
        p1 = 0
        p2 = 1
        p3 = 1
        if n == 0:
            return 0
        for i in range(n - 2):
            temp1 = p3
            p3 = p1 + p2 + p3
            p1 = p2
            p2 = temp1
        return p3