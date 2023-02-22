class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    
        window = Counter()
        left = 0
        ans = 0
        for i,ch in enumerate(s):
            window[ch] += 1
        
            if window[ch] > 1:
                while window[ch] > 1 and left < i:
                    window[s[left]] -= 1
                    left += 1
            else:
                ans = max(ans, i - left + 1)
                    
        return ans        
                    
                
        
        