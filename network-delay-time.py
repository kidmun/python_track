class Solution:
    def networkDelayTime(self, edges: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        cost = {}
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            cost[(edges[i][0], edges[i][1])] = edges[i][2]
           
        
        heap = []
        visited = set([k])
        ans = -1
        for el in graph[k]:
            heappush(heap, (cost[(k, el)], el))
        while heap:
            cur = heappop(heap)
            ans = max(ans, cur[0])

            visited.add(cur[1])
            if len(visited) == n:
                return ans
            for el in graph[cur[1]]:
                if el not in visited:
                    heappush(heap, (cost[(cur[1], el)] + cur[0], el))
        return -1