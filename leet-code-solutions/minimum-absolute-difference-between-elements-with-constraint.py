from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        ss = SortedList([])
        ans = float("inf")
        n = 0
        ind = 0

        for i in range(x, len(nums)):
            ss.add(nums[ind])
            n += 1
            left = ss.bisect_left(nums[i])
            right = ss.bisect_right(nums[i])
            # print(ss, left, right, nums[i])
            if left == right:
                ans = min(ans,abs(nums[i] - ss[max(0,left - 1)]), abs(ss[min(n - 1, right)] - nums[i]))
            else:
                return 0
            ind += 1
        return ans
       