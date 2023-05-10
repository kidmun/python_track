class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        graph = defaultdict(list)
        degree = Counter()
        for i, r in enumerate(recipes):
            for ing in ingredients[i]:
                graph[ing].append(r)
                degree[r] += 1
        queue = deque([])
        visited = set([])
        for sup in supplies:
            queue.append(sup)
            visited.add(sup)
        
        ans = []
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                ans.append(cur)
                for ne in graph[cur]:
                    if ne not in visited and degree[ne] < 2:
                        queue.append(ne)
                        visited.add(ne)
                    degree[ne] -= 1
        return ans[len(supplies):]