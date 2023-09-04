class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}
        def dp(start, cur):
            if cur > amount:
                return 0
            if cur == amount:
                return 1
            if (cur, coins[start]) in memo:
                return memo[(cur, coins[start])]
            val = 0
            for i in range(start, len(coins)):
                val += dp(i, cur + coins[i])
            memo[(cur, coins[start])] = val
            return memo[(cur, coins[start])]
        return dp(0, 0)