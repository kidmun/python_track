class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        nums = list(count.keys())
    
        def quickSort(arr):
            print(arr)
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            pivot = arr[mid]
            l = [x for x in arr if count[x] > count[pivot]]
            middle = [x for x in arr if count[x] == count[pivot]]
            r = [x for x in arr if count[x] < count[pivot]]
            return quickSort(l) + middle + quickSort(r)
        ans = quickSort(nums)
   
        return ans[:k]