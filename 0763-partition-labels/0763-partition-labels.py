class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left = 0
        ans = []
        while left < len(s):
            right = s.rfind(s[left])
            i = left + 1
            
            while i < right:
                val = s.rfind(s[i])
                right = max(right, val)
                i += 1
            
            ans.append(right - left + 1)
            left = right + 1
        return ans