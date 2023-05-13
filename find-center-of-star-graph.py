class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for ed in edges:
            graph[ed[0]].append(ed[1])
            graph[ed[1]].append(ed[0])
        for key in graph:
            if len(graph[key]) == len(edges):
                return key