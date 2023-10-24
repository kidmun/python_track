class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # graph = defaultdict(list)
        # graph[0].append((firstPerson, 0))
        # for a, b, t in meetings:
        #     graph[a].append((b, t))
        #     graph[b].append((a, t))
        # stack = [(0, -1)]
        # mi = {}
        # for i in range(n):
        #     mi[i] = float("inf")
        # mi[0] = 0
        # while stack:
        #     cur, par = stack.pop()
        #     for ch, t in graph[cur]:
        #         if t >= mi[cur] and ch != par and mi[ch] > t:
        #             mi[ch] = t
        #             stack.append((ch, cur))
        # count = []
        # for key in mi:
        #     if mi[key] != float("inf"):
        #         count.append(key)
        # return count
        parent  ={}
        rank = {}
        for i in range(n):
            parent[i] = i
            rank[i]= 1
        dic = defaultdict(list)
        dic[0].append((0, firstPerson))
        for a, b, t in meetings:
            dic[t].append((a, b))
        def find(word):
            if parent[word] != word:
                parent[word] = find(parent[word])
            return parent[word]
        def union(word1, word2):
            par_word1 = find(word1)
            par_word2 = find(word2)
            if rank[par_word1] >= rank[par_word1]:
                rank[par_word1] += rank[par_word2]
                parent[par_word2] = par_word1
            else:
                rank[par_word2] += rank[par_word1]
                parent[par_word1] = par_word2
        keys = sorted(dic)
        ans= set()
        for key in keys:
            for a, b in dic[key]:
                union(a, b)
            for a, b in dic[key]:
                if find(a) == find(0):
                    ans.add(a)
                    ans.add(b) 
                else:
                    parent[a] = a
                    parent[b] = b       
        return list(ans)