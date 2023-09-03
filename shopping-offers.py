class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        ans = float("inf")
        count = 0
        memo = {}
        def backtrack(p, cur):
            nonlocal ans
            xx = tuple(cur)
            if xx in memo:
                return memo[xx]    
            v = 0
            for i in range(n):
                v += (needs[i] - cur[i]) * price[i]
            for i in range(len(special)):
                new = cur[::]
                flag = True
                for j in range(len(special[i]) - 1):
                    new[j] += special[i][j]
                    if new[j] > needs[j]:
                        flag  = False
                        break
                if flag:
                    v = min(v, backtrack(p, new) + special[i][-1])
            memo[xx] = v
            return memo[xx] 
        return backtrack([], [0] * n)