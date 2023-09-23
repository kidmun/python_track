class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) < k:
            return []
        heap = []
        for i in range(k):
            heappush(heap, ( -(abs(arr[i] - x)), -arr[i]))
        for i in range(k, len(arr)):
            heappushpop(heap, ( - (abs(arr[i] - x)), -arr[i]))
        for i in range(k):
            arr[i] = -heappop(heap)[1]
        return sorted(arr[:k])