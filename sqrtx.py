class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right  = x
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 == x or ((mid + 1) ** 2 > x and mid ** 2 and mid ** 2 < x):
                return mid
            elif mid ** 2 < x:
                left = mid + 1
            elif mid ** 2 > x:
                right = mid - 1