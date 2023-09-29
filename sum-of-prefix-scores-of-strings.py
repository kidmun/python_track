class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = True
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for ch in word:
            if not cur.children[ord(ch) - 97]:
                cur.children[ord(ch) - 97] = TrieNode()
            cur = cur.children[ord(ch) - 97]
            cur.count += 1
    def count(self, word):
        cur = self.root
        total = 0
        for ch in word:
            if not cur.children[ord(ch) - 97]:
                cur.children[ord(ch) - 97] = TrieNode()
            cur = cur.children[ord(ch) - 97]
            total += cur.count
        return total


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        for w in words:
            t.insert(w)
        ans = []
        for w in words:
            ans.append(t.count(w))
        return ans