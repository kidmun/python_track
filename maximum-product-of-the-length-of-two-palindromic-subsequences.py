class Solution:
    def maxProduct(self, s: str) -> int:
        memo = {}
        def dp(s, l, r):
            
            if l >= r:
                return 1 -(l - r)
            if (s, l, r) in memo:
                return memo[(s, l, r)]
            if s[l] == s[r]:
                memo[(s, l, r)] = 2 + dp(s, l + 1, r - 1)
            else:
                memo[(s, l, r)] = max(dp(s, l,  r- 1), dp(s, l + 1, r))
            return memo[(s, l, r)]

        ans = 0
        def backtrack(index, subsequence1, subsequence2):
            nonlocal ans
            if index == len(s):
                ans = max(ans, dp(subsequence1, 0, len(subsequence1) - 1, ) * dp(subsequence2, 0, len(subsequence2) - 1))
                return
            char = s[index]

    
            backtrack(index + 1, subsequence1 + char, subsequence2)

          
            backtrack(index + 1, subsequence1, subsequence2 + char)

        all_subsequences = []
        backtrack(0, "", "")
        return ans