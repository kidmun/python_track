class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = []
        for i, interval in enumerate(intervals):
            starts.append((interval[0], i))
            intervals[i] = interval[1]
            
        starts.sort()
      
        for i, end in enumerate(intervals):
            left = 0
            right = n - 1
            ans = -1
            while left <= right:
                mid = (left + right) // 2         
                if starts[mid][0] >= end:
                    ans = starts[mid][1]
                    right = mid - 1
                else:
                    left = mid + 1
            intervals[i] = ans
        return intervals