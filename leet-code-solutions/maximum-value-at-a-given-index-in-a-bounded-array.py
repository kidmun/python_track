class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        low = 1
        high = maxSum
        def checker(num, val):
            total = (num - 1) * (num) // 2
            if val > (num - 1):
                total += (val  - (num - 1))
            else:
                x = num - 1 - val
                total -= (x * (x + 1) // 2)
            return total
        xx = n - index - 1
        while low <= high:
            mid = (low + high) // 2
            if checker(mid, index) + checker(mid, xx) + mid <= maxSum:
                low  = mid + 1
            else:
                high = mid - 1
        # print(checker(6, 2),checker(6, 1))
        return high
             

        