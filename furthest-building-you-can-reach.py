class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        index = []
        for ind in range(len(heights) - 1):
            if heights[ind] < heights[ind + 1]:
                index.append((heights[ind + 1] - heights[ind], ind))
        heap = []
        i = 0
        while i < len(index) and i < ladders:
            heappush(heap, index[i])
            i += 1
        cur = 0
        while i < len(index):
            heappush(heap, index[i])
            val = heappop(heap)
            if cur + val[0] > bricks:
                return index[i][1]
            i += 1
            cur += val[0]
        return len(heights) - 1