class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        window = Counter(s2[:len(s1)])
       
        if window == count:
            return True
        window[s2[0]] -= 1
        if window[s2[0]] == 0:
            del window[s2[0]]
        left = 1
        right = len(s1)
        while right < len(s2):
            
            window[s2[right]] += 1
         
            if window == count:
                return True
            window[s2[left]] -= 1
            if window[s2[left]] == 0:
                del window[s2[left]]
            right += 1
            left += 1
            
        return False
