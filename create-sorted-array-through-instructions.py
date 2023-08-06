class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def countSmaller(nums, count):
            def mergeSort(left, right):
                if left >= right:
                    return [(nums[left], left)]
                mid = (left + right) // 2
                l = mergeSort(left, mid)
                r = mergeSort(mid + 1, right)
                return merge(l, r)
                
            def merge(left, right):
                arr = [0] * (len(left) + len(right))
                p1 = 0
                p2 = 0
                l = len(left)
                r = len(right)
                l1 = l - 1
                r1 = r - 1
                 
                for i in range(len(arr)):
                    if p1 < l and (p2 >= r or left[p1][0] <= (right[p2][0])):
                        arr[i] = left[p1]
                        p1 += 1
                    else:
                        arr[i] = right[p2]
                        count[right[p2]][0] += (len(left) - p1)          
                        p2 += 1
                    if l1 > -1 and (r1 < 0 or left[l1][0] >= right[r1][0]):
                        l1 -= 1
                    else: 
                        count[right[r1]][1] += (l1 + 1)
                        r1 -= 1
                    
                return arr
            mergeSort(0, len(nums) - 1)
        ans = 0
        count = {}
        for i, num in enumerate(instructions):
            count[(num, i)] = [0, 0]
        countSmaller(instructions, count)
        for key in count:
            ans += min(count[key])
        return ans % (10 ** 9 + 7)