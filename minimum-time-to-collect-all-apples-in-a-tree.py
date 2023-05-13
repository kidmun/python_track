class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        graph = defaultdict(list)
        for ed in edges:
            graph[ed[0]].append(ed[1])
            graph[ed[1]].append(ed[0])
        def dfs(node, par):
            value = 0

            for ne in graph[node]:
                if ne == par:
                    continue
                value += dfs(ne, node)
          
            if node == 0:
                return value
            if value > 0:
                return value + 2
            if hasApple[node]:
                return 2
            return 0
        return dfs(0, -1)