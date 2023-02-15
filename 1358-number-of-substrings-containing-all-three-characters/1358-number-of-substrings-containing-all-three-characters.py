class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        left = 0
        count = Counter()
        ans = 0
        for i, c in enumerate(s):
            count[c] += 1
            if count["a"] >= 1 and count["b"] >= 1 and count["c"] >= 1:
                
                ans += (n - i)
              
                count[s[left]] -= 1
                left += 1
                while count["a"] >= 1 and count["b"] >= 1 and count["c"] >= 1 and left < i:
                    ans += (n - i)
                    count[s[left]] -= 1
                    left += 1
        return ans
                    
                    
                
                
            
            
        