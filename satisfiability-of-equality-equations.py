class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
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
        for eq in equations:
            if eq[1] == "=":
                union(ord(eq[0]), ord(eq[3]))
        assign = [0] * 26
        count = 1
        for i in range(26):
            if assign[i] == 0:
                assign[i] = count
                for j in range(26):
                    if find(97 + i) == find(97 + j) and i != j:
                        assign[j] = count
                count += 1
        for eq in equations:
            if eq[1] == "!" and assign[ord(eq[0]) - 97] == assign[ord(eq[3]) - 97]:
                return False
        return True