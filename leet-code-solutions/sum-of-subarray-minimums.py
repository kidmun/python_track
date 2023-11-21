class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        arr = arr + [0]
        stack = [-1]
        ans = 0
        for i in range(n):
            while stack and arr[i] <= arr[stack[-1]]:
                val = stack.pop()
                ans += (val - stack[-1]) * (i - val) * arr[val]
            stack.append(i)
        # print(stack, ans)
        for i in range(1, len(stack)):
            ans += (stack[i] - stack[i - 1]) * (n - stack[i]) * arr[stack[i]]
        return ans % (10 ** 9 + 7)



        


    
        