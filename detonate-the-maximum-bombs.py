class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        n = len(bombs)
        def checkIntersection(circle1, circle2):
            d = ((circle2[1] - circle1[1]) ** 2 + (circle2[0] - circle1[0]) ** 2 )**0.5
            r1 =  circle1[2]
            r2 = circle2[2]
            return r1 >= d 
        for i in range(n):
            for j in range(n):
                if i != j and checkIntersection(bombs[i], bombs[j]):
                    graph[i].append(j)
        def dfs(circle, visited):
            nonlocal ans, count
            count += 1
            for cir in graph[circle]:
                if cir not in visited:
                    visited.add(cir) 
                    dfs(cir, visited)
        count = 0 
        ans = 0
        for i in range(n):
            count = 0
            dfs(i, set([i]))
            ans = max(ans, count)
        return ans