class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)
        for i in range(len(questions) - 1, -1, -1):
            val1=  0
            if (1 + i + questions[i][1]) < len(questions):
                val1 = dp[i + questions[i][1] + 1] 
            dp[i] = max(dp[i + 1], val1 + questions[i][0])
        return dp[0]