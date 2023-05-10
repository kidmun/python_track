class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = [0] * numCourses
        graph = defaultdict(list)
        for c, pre in prerequisites:
            graph[pre].append(c)
            degree[c] += 1
        queue = deque([])
        ans = []
        for i, d in enumerate(degree):
            if d == 0:
                queue.append(i)
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                ans.append(cur)
                for num in graph[cur]:
                    if degree[num] < 2:
                        queue.append(num)
                    degree[num] -= 1
        if len(ans) < numCourses:
            return []
        return ans