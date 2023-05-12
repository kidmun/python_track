class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = []
        for pile in piles:
            heappush(heap, -1 * pile)
        for i in range(k):
            if heap:
                val = heappop(heap)
                heappush(heap, val  + -1 * val // 2)
        return -1 * sum(heap)