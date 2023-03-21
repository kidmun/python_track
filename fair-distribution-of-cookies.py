class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
      
        ans = float('inf')
        cur = [0] * k
        def backtrack(ind):
            nonlocal cur, ans
            if ind >= len(cookies):
                ans = min(ans, max(cur))
                return 
            if ans <= max(cur):
                return 
            for j in range(k):
                cur[j] += cookies[ind]
                backtrack(ind + 1)
                cur[j] -= cookies[ind]
        backtrack(0)
        return ans