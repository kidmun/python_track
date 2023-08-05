class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        if satisfaction[-1] <= 0:
            return 0
        total = sum(satisfaction)
        ind = None
        for i in range(n):
            if total < 0:
                total -= satisfaction[i]
            else:
                ind = i
                break
          
        ans = 0
        count = 1
        for x in range(ind, n):
            ans += count * satisfaction[x]
            count += 1
        return ans