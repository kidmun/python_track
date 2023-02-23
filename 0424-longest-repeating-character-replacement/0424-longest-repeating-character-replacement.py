class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = Counter()
        larg = 0
        left = 0
        ans = 1
        for i, ch in enumerate(s):
 
            count[ch] += 1
            if count[ch] > larg:
                larg = count[ch]
            if larg > ans:
                ans = larg
            if (i - left + 1 - larg) > k or i == (len(s) - 1):

                if i == (len(s) - 1) and (i - left + 1 - larg) <= k:
                    ans = max(ans, i - left + 1)
                else:
                    ans = max(ans, i - left)
                if count[s[left]] == larg:
                    count[s[left]] -= 1
                    larg = max(count.values())
                else:
                    count[s[left]] -= 1 
                left += 1
        return ans
                    
            
        