class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        x = []
        y = []
        for i in range(len(nums1)):
            x.append(nums1[i] - nums2[i])
        def countSmaller(nums, diff):
            count = Counter()
            def mergeSort(left, right):
                if left >= right:
                    return [(nums[left], left)]
                mid = (left + right) // 2
                l = mergeSort(left, mid)
                r = mergeSort(mid + 1, right)
                return merge(l, r)
            def merge(left, right):
                nonlocal count
                arr = [0] * (len(left) + len(right))
                i = 0
                p1 = 0
                p2 = 0
                while i < len(arr):
                    if p1 < len(left) and (p2 >= len(right) or left[p1][0] <= (right[p2][0])):
                        arr[i] = left[p1]
                        p1 += 1
                    else:
                        arr[i] = right[p2]
                        p2 += 1
                    i += 1
                i = 0
                p1 = 0
                p2 = 0
                while i < len(arr):
                    if p1 < len(left) and (p2 >= len(right) or (left[p1][0] -diff) <= (right[p2][0])):
                        count[left[p1]] += (len(right) - p2)
                        p1 += 1
                    else:
                        p2 += 1
                    i += 1
                return arr
            val = mergeSort(0, len(nums) - 1)
            ans = []
            
            for i, num in enumerate(nums):
                ans.append(count[(num, i)])
            return ans
        return sum(countSmaller(x, diff))