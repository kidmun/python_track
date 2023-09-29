# class TrieNode:
#     def __init__(self):
#         self.children = [None] * 2
        
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#     def insert(self, num, ma):
#         cur = self.root
#         for i in range(ma, -1, -1):
#             v = 1 if (num & (1 << i)) > 0 else 0
#             if not cur.children[v]:
#                 cur.children[v] = TrieNode()
#             cur = cur.children[v]
#     def findMax(self, num, res, ma):
#         cur = self.root
#         for i in range(ma, -1, -1):
#             v = 1 if (num & (1 << i)) > 0 else 0
#             if cur.children[1 - v]:
#                 res = res | 1 << i
#                 cur = cur.children[1 - v]
#             else:
#                 cur = cur.children[v]
#         return res

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        t = {}
        m = max(nums)
        ma = ceil(log(m if m > 0 else 1 , 2))
        for num in nums:
            cur = t
            for i in range(ma, -1, -1):
                v = 1 if (num & (1 << i)) > 0 else 0
                if v not in cur:
                    cur[v] = {}
                cur = cur[v]
        
        ans = 0
        for num in nums:
            res = 0
            cur = t
            for i in range(ma, -1, -1):
                v = 1 if (num & (1 << i)) > 0 else 0
                if (1 -v) in cur:
                    res = res | 1 << i
                    cur = cur[1 - v]
                else:
                    cur = cur[v]
            ans = max(ans, res)
        return ans