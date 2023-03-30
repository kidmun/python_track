class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(int(math.log(num, 2)) + 1):
            num = num ^ (1<<i)
        return num