class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        timePoints.sort()
        ans = float("inf")
        for i in range(1, n):
            x, y = timePoints[i], timePoints[i - 1]
            ans = min(ans, 60 * (int(x[:2]) - int(y[:2])) + (int(x[3:]) - int(y[3:])))
        x, y = timePoints[0], timePoints[-1]
        v = (24  - int(y[:2]) - 1) * 60 + 60 - int(y[3:]) + int(x[:2]) * 60 + int(x[3:])
        return min(ans, v)
        