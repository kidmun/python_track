class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans = 0
        stack = []
        n = len(arr)   
        for i, num in enumerate(arr):
            ans += num
            if stack:
                while stack and stack[-1][0] > num:
                    val = stack.pop()
                    if stack:
                        elem = (val[1] - stack[-1][1] - 1)
                        ans += (val[0] * elem)                
                    else:
                        elem = val[1]
                        ans += (val[0] * elem)
                    ans += val[0] * (i - val[1] - 1)
                    ans += val[0] * (i - val[1] - 1) * elem
            stack.append((num, i))
        for i, s in enumerate(stack):
            if i == 0:
                val = n - s[1] - 1
                ans += (s[0] * (s[1]))
                ans += s[0] * (val + val*s[1]) 
            else:
                val = n - s[1] - 1
                ans += (s[0] * (s[1] - stack[i-1][1] - 1))
                ans += s[0] * (val + val*(s[1] - stack[i-1][1] - 1)) 
    
        return ans % (10**9 + 7)