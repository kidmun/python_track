class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 1
        ans = None
        right = sum(weights)
        while left <= right:
            mid = (left + right) // 2
            count = 1
            cur = 0
            flag = True
            for w in weights:
                if (cur + w) > mid:
                    count += 1
                    cur = 0
                    if w > mid:
                        flag = False
                        break
                cur += w
            if count > days or not flag:
                left = mid + 1     
            else:
                ans = mid
                right = mid - 1
                
        return ans