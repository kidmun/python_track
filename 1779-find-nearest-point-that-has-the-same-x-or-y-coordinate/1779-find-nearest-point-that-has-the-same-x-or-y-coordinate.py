class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = []
        count = 0
        obj = {}
        for p in points:
            if x == p[0] or y == p[1]:
                dis = abs(x-p[0]) + abs(y-p[1])
                ans.append(dis)
                obj[count] = dis
                
            count += 1
        if len(ans) == 0:
            return -1
        ans.sort()
        for index in obj:
            if obj[index] == ans[0]:
                return index
                
        