class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(ind, cur, track):
            if "".join(track) == s:
                return True
            for i in range(ind, len(s)):
                if (cur - 1) == int(s[ind:i + 1]):
                    track.append(s[ind:i + 1])
                    if backtrack(i+1, int(s[ind:i + 1]),track):
                        return True
                    track.pop()
            return False
        for i in range(0, len(s)- 1):
            if backtrack(i + 1, int(s[:i+1]), [s[:i+1]]):
                return True
     
        return False