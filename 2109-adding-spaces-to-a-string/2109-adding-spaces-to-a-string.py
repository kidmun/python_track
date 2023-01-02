class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        count = 0 
        ans = ""
        for i in range(len(s)):
            if count < len(spaces):
                if spaces[count] == i:
                    ans += " "
                    count += 1
            ans += s[i]
        return ans
        