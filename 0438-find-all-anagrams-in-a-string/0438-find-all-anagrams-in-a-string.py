class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        window = Counter(s[:len(p)])
        left = 1
        ans = []
        if window == target:
            ans.append(0) 
        window[s[0]] -= 1
        for i in range(len(p), len(s)):
            window[s[i]] += 1
            if window == target:
                ans.append(left)
            window[s[left]] -= 1
            left += 1
           
        return ans
                
            
        