class Solution:
    def knightDialer(self, n: int) -> int:
        def inbound(row, col):
            return (0 <= row < 3 and 0 <= col < 3) or (row == 3 and col == 1)
        directions = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        memo = {}
        def dp(row, col, ind):
            if ind == n:
                return 1
            if (row, col, ind) in memo:
                return memo[ (row, col, ind)]
            val = 0
            for a, b, in directions:
                x, y = a + row, b + col
                if inbound(x, y):
                    val += dp(x, y, ind + 1)
            memo[ (row, col, ind)] = val
            return memo[ (row, col, ind)]
        ans = dp(3, 1, 1)
        for i in range(3):
            for j in range(3):
                ans += dp(i, j, 1)


        return ans % (10 ** 9 + 7)