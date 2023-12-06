class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:


        graph = defaultdict(list)
        for i, num in enumerate(manager):
            graph[num].append(i)
        
        stack = [(headID, 0)]
        ans = 0
        while stack:
            cur = stack.pop()
            if len(graph[cur[0]]) == 0:
                ans = max(ans, cur[1])
            for ne in graph[cur[0]]:
                stack.append((ne, cur[1] + informTime[cur[0]]))
        return ans


        