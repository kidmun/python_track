class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False
        self.score = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.dic = {}
    def insert(self, word, val):
        cur = self.root
        
        for ch in word:
            if not cur.children[ord(ch) - 97]:
                cur.children[ord(ch) - 97] = TrieNode()
            cur = cur.children[ord(ch) - 97]
            if word in self.dic:
                cur.score -= self.dic[word]
            cur.score += val
        self.dic[word]  = val
    def calculateSum(self, prefix):
    
        cur = self.root
        for ch in  prefix:
            if not cur.children[ord(ch) -97]:
                return 0
            cur = cur.children[ord(ch) -97]
            
        return cur.score
               
class MapSum:

    def __init__(self):
        
        self.trie = Trie()
        

    def insert(self, key: str, val: int) -> None:
        self.trie.insert(key, val)

        

    def sum(self, prefix: str) -> int:
        return self.trie.calculateSum(prefix)

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)