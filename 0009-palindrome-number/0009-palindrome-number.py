class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        ans = []
        for s in str_x:
            ans.append(s)

        rev_x = ""
        for s in range(len(ans)):
            rev_x += ans.pop()
        return rev_x == str_x


