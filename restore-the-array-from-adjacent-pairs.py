class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
        stack = []
        for key, li in graph.items():
            if len(li) == 1:
                stack.append(key)
                break
        ans = []
        visited = set([stack[0]])
        while stack:
            cur = stack.pop()
            ans.append(cur)
            for ne in graph[cur]:
                if ne not in visited:
                    stack.append(ne)
                    visited.add(ne)
        return ans