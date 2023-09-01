class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1] * n
        inc = [1] * n
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                inc[i] += inc[i + 1]
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                ans[i + 1] = ans[i] + 1
            elif ratings[i] > ratings[i + 1]:
                ans[i] = max(inc[i], ans[i])
        return sum(ans)