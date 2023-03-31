class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = False
        if (n & (1<<0)):
            prev = True
        for i in range(1, int(math.log(n, 2))+1):
            if n & (1<<i):
                if prev:
                    return False
                prev = True
            else:
                if not prev:
                    return False
                prev = False
            
        return True