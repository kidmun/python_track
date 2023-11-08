class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i, e in enumerate(equations):
            graph[e[0]].append((e[1], values[i]))
            graph[e[1]].append((e[0], 1/ values[i]))
        ans = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                ans.append(-1.0)
            elif q[0] == q[1]:
                ans.append(1.00000)
            else:
                
                stack = [(q[0], 1)]
                cur_res = 1
                visited = set([q[0]])
                flag = False
                while stack:
                    print(stack, q)
                    cur = stack.pop()
                    for val in graph[cur[0]]:
                        if val[0] not in visited:
                            visited.add(val[0])
                            stack.append((val[0], val[1] * cur[1]))
                            if val[0] == q[1]:
                                ans.append(val[1] * cur[1])
                                flag =True
                                break
                if not flag:
                    ans.append(-1.0)
        return ans
            



