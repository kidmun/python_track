class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1, p2 = 0, 0
        while p1 < len(s):
            while p2 < len(t) and s[p1] != t[p2]:
                p2 += 1
            if p2 >= len(t):
                return False
            p1 += 1
            p2 += 1
        return True


        

        