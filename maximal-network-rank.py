class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        s = set([])
        for r in roads:
            s.add(tuple(r))
        edges = defaultdict(list)
        for r in roads:
            edges[r[0]].append(r[1])
            edges[r[1]].append(r[0])
        ans = 0
        for key1 in edges:
            for key2 in edges:
                if key1 != key2:
                    value = len(edges[key2]) + len(edges[key1])
                    if (key1, key2) in s or (key2, key1) in s:
                        value -= 1 
                    ans = max(value, ans)
        return ans