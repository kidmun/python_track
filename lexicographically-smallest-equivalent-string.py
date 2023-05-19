class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent =  {}
        rank = [1] * 26
        for i in range(97, 97 + 26):
            parent[i] = i
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if rank[x - 97] >= rank[y - 97]:
                    rank[x - 97] += rank[y - 97]
                    parent[parent_y] = parent_x
                else:
                    rank[y- 97] += rank[x - 97]
                    parent[parent_x] = parent_y
        for i in range(len(s1)):
            union(ord(s1[i]), ord(s2[i]))
        ans = ""

        for i in range(len(baseStr)):
            for j in range(97, 97 + 26):
                if find(ord(baseStr[i])) == find(j):
                    ans += chr(j)
                    break
        return ans