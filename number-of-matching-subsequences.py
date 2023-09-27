class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end_word = False
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = 0
        
    def insert(self, word):
        cur = self.root
        for ch in word:
            if not cur.children[ord(ch) - 97]:
                cur.children[ord(ch) - 97] = TrieNode()
            cur = cur.children[ord(ch) - 97]
        cur.end_word = True
        cur.count += 1
    def findInde(self, word, start, ch):
        for i in range(start, len(word)):
            if word[i] == ch:
                return i
        return -1
    def dfs(self, word,cur, ind, xx):
        for i in range(26):
            if cur.children[i]:
                child = cur.children[i]
                val = self.findInde(word, ind, chr(97 + i))
                if val != -1:
                    if child.end_word:  
                        self.ans += child.count
                    self.dfs(word, child, val + 1, xx  + chr(97 + i))
              


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        t = Trie()

        for w in words:
            t.insert(w)

        t.dfs(s, t.root, 0, "")
       
        return t.ans