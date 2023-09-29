class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.EndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        cur = self.root
        for i, ch in enumerate(word):
            if not cur.children[ord(ch) - 97]:
                cur.children[ord(ch) - 97] = TrieNode()
            cur = cur.children[ord(ch) - 97]
        cur.EndOfWord = True
   
    def searchW(self, word: str) -> bool:
        cur = self.root
        for i, ch in enumerate(word):
            cur = cur.children[ord(ch) - 97]
            if not cur.EndOfWord:
                return False
        return True
class Solution:
    def longestWord(self, words: List[str]) -> str:
        t = Trie()
        ans = []
        memo = set([])
        for w in words:
            t.insert(w)
        ma = 1
        for w in words:
            if t.searchW(w) and w[:len(w) - 1] not in memo:
                ans.append((-len(w), w))
                ma = max(ma, len(w))
            else:
                memo.add(w)
        ans.sort()
        return ""  if not ans else ans[0][1]