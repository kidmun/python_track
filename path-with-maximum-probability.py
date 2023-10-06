class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        cost = {}
        dis = [0] * n
        for i in range(len(edges)):
            graph[edges[i][1]].append(edges[i][0])
            graph[edges[i][0]].append(edges[i][1])
            cost[(edges[i][0], edges[i][1])] = succProb[i]
            cost[(edges[i][1], edges[i][0])] = succProb[i]
        
        heap = [(-1, start_node)]
        visited = set([start_node])
      
        while heap:
            cur = heappop(heap)
            # print(cur)
            if cur[1] == end_node:
                return -cur[0]
            visited.add(cur[1])
            for el in graph[cur[1]]:
                if el not in visited and cost[(el, cur[1])] * -cur[0] > dis[el]:
                    dis[el] = cost[(el, cur[1])] * cur[0]
                    heappush(heap, (cost[(el, cur[1])] * cur[0], el))
        return 0