class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0

        x = x ^ y
        if x == 0:
            return 0
        for i in range(int(math.log(x, 2))+1):
            if x & (1 << i):
                count += 1
        return count