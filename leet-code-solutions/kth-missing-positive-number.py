class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        count = 0
        arr = [0] + arr
        total = 0
       
        for i in range(len(arr) - 1):
       
            if total + (arr[i + 1] - arr[i] - 1) >= k:
                return arr[i] + k - total
            total += (arr[i + 1] - arr[i] - 1)

        return arr[-1] + k - total
        

        