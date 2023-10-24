class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        parent  ={}
        rank = {}
        for w in strs:
            parent[w] = w
            rank[w]= 1
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
        def checker(i, j):
            count = 0
            for k in range(len(strs[i])):
                if strs[i][k] != strs[j][k]:
                    count += 1
            return 2 >= count        
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if checker(i, j):
                    union(strs[i], strs[j])
        ss = set()
        for key in parent:
            ss.add(find(key))
        return len(ss)