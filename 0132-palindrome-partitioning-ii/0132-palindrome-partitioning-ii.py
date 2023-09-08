class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        def backtrack(start):
            if start >= len(s):
                return 0
            if start in memo:
                return memo[start]
            cur = ""
            val = float("inf")
            for i in range(start, len(s)):
                
                cur += s[i]
                if cur == cur[::-1]:
                    val = min(backtrack(i + 1), val)
        
            memo[start] = val + 1
            return  memo[start] 
            
        return backtrack(0) - 1
      