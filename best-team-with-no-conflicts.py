class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)    
        scores = [(ages[i], scores[i]) for i in range(n)]
        scores.sort()   
        dp = [0] * n 
        dp[0] = scores[0][1]  
        for i in range(1, n):
            dp[i] = scores[i][1]
            for j in range(i):
                if scores[j][1] > scores[i][1]:
                    continue
                dp[i] = max(dp[i], scores[i][1] + dp[j])
       
        return max(dp)