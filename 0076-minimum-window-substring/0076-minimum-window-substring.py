class Solution:
    def checkEqual(self, window, count):
        if len(window) == len(count):
            flag = True
            for key, amount in count.items():
                if window[key] < amount:
                    flag = False
            if flag:
                return flag
        return False
        
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        left = 0
        window = Counter()
        ans = [0, len(s) + 1]
        for i, ch in enumerate(s):
            
            if ch in count:
                window[ch] += 1
                

            if self.checkEqual(window, count):
                
                if (i - left + 1) < (ans[1] - ans[0]):
                    ans = [left, i + 1]
                if s[left] in count:
                    window[s[left]] -= 1
                    if window[s[left]] == 0:
                        del window[s[left]]
                left += 1
                while self.checkEqual(window, count) and left <= i:
                    if (i - left + 1) < ans[1] - ans[0]:
                        ans = [left, i + 1]
                    if s[left] in count:
                        window[s[left]] -= 1
                        if window[s[left]] == 0:
                            del window[s[left]]
                    left += 1
        if ans[1] - ans[0] > len(s):
            return ""
        else:
            return s[ans[0]:ans[1]]
               
        
        