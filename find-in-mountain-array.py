# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        low = 0
        high = n - 1
        ans = float("inf")
        while low <= high:
            mid = (low + high) // 2
            x = mountain_arr.get(mid)
            y = float("-inf")
            z = float("inf")
            if mid > 0:
                y = mountain_arr.get(mid - 1)
            if mid < n - 1:
                z = mountain_arr.get(mid + 1)
            # print(x, low, high)
            if y < x < z:
                if x == target:
                    ans = min(ans, mid)
                    high = mid - 1
                elif x > target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if x == target:
                    ans = min(ans, mid)
                high = mid - 1
        low = 0
        high = n - 1
        # ans = float("inf")
        while low <= high:
            mid = (low + high) // 2
            x = mountain_arr.get(mid)
            y = float("inf")
            z = float("-inf")
            if mid > 0:
                y = mountain_arr.get(mid - 1)
            if mid < n - 1:
                z = mountain_arr.get(mid + 1)
            # print(x, low, high)
            if y > x > z:
                if x == target:
                    ans = min(ans, mid)
                    high = mid - 1
                elif x > target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if x == target:
                    ans = min(ans, mid)
                low = mid + 1
        return ans if ans != float("inf") else -1