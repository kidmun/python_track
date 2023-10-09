class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        count = 0
        visited = set()
        memo = {}
        def dp(cur, par):
            nonlocal count
            if cur in memo:
                return memo[cur]
            if len(graph[cur]) == 1:
                if values[cur] % k == 0:
                    count += 1
                    memo[cur] = 0
                    return 0
                memo[cur] = values[cur]
                return values[cur]
            val = values[cur]
            for ne in graph[cur]:
                if ne != par:
                    val += dp(ne, cur)
            if val % k == 0:
                count += 1       
                memo[cur] = 0
            else:
                memo[cur] = val
            return memo[cur]
        for i in range(n):
            if i not in memo:
                memo[i] = dp(i, -1)

      
        return count