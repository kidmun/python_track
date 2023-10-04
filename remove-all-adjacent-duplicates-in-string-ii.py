class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        prev = 0
        c = None
        for i in range(len(s)):
            if not stack or stack[-1][0] != s[i]:
                stack.append((s[i], 1))
            else:
                stack.append((s[i], stack[-1][1] + 1))
                
            if stack and stack[-1][1] >= k:
                x = k
                while x > 0:
                    stack.pop()
                    x -= 1
        ans = ""
        for s in stack:
            ans += s[0]
        return ans