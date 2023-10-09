class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        cost = {}
        for i in range(len(flights)):
            graph[flights[i][0]].append(flights[i][1])
            cost[(flights[i][0], flights[i][1])] = flights[i][2]
        distance = [float("inf")] * n
        heap = [(0, 0, src)]
        while heap:
            a, b, c = heappop(heap)
          
            if c == dst:
                return a
            distance[c] = b
            for ne in graph[c]:
                if b <= k and distance[ne] >= b + 1:
                    heappush(heap, (a + cost[(c, ne)], b + 1, ne))   
        return -1