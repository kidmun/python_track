class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def backtrack(start, container):
            nonlocal ans
            ans = max(ans, len(container))
            if start > len(arr):
                return 
            for i in range(start, len(arr)):
                flag = False
                for ch in arr[i]:
                    if ch in container:
                        flag = True
                if len(Counter(arr[i])) < len(arr[i]):
                    flag = True
                if not flag:
                    for ch in arr[i]:
                        container.add(ch)
                backtrack(i + 1,container)
                if not flag:
                    for ch in arr[i]:
                        container.remove(ch)
        ans = 0
        s = set()
        backtrack(0, s)
        return ans