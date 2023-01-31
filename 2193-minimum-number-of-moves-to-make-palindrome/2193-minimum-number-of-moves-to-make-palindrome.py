class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        left = 0
        right = n - 1
        res = 0
        s = list(s)
        count = 0
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                p1 = left + 1
                p2 = right - 1
                while s[p2] != s[left] and s[p1] != s[right]:
                    p2 -= 1
                    p1 += 1
                    
                if s[p2] == s[left] and s[p1] == s[right]:
                 
                    val = s.pop(p1)
                    s.insert(left, val)
                    count += (p1 - left)
                elif s[p2] == s[left]:
                    val = s.pop(p2)
                    s.insert(right, val)
                    count += (right - p2)
                else:
                    val = s.pop(p1)
                    s.insert(left, val)
                    count += (p1 - left)
                    left += 1
                    right -= 1
                    
                
    
                    
        return count