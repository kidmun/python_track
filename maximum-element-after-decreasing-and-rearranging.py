class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        i = 1
        arr[0] = 1
        while i < len(arr):
            if arr[i] - arr[i - 1] > 1:
                arr[i] = arr[i-1] + 1
            i += 1
        return arr[-1]