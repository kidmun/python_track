class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for ch in s:
            if ch == "#":
                if s1:
                    s1.pop()
            else:
                s1.append(ch)
        for ch in t:
            if ch == "#":
                if s2:
                    s2.pop()
            else:
                s2.append(ch)
        
        return s1 == s2
        