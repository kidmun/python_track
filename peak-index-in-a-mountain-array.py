class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        right = n - 1
    
        while left <= right:
            mid = (left + right) // 2
            if mid == 0 or (arr[mid - 1] < arr[mid] and arr[mid+1] > arr[mid]):
                left = mid + 1
            elif mid == (n-1) or (arr[mid - 1] > arr[mid] and arr[mid+1] < arr[mid]):
                right = mid - 1
            else:
                return mid