class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.EndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str) -> None:
        cur = self.root
        for i, ch in enumerate(word):
            if not cur.children[ord(ch) - 97]:
                cur.children[ord(ch) - 97] = TrieNode()
            cur = cur.children[ord(ch) - 97]
        cur.EndOfWord = True
        

    def search(self, word: str) -> bool:
     
        cu = self.root
        def dfs(i, cur):
            if i >= len(word):
                return cur.EndOfWord
            if word[i] == ".":
                flag = False
                for j in range(26):
                    if cur.children[j]:
                        if dfs(i + 1,cur.children[j]):
                            return True
                return False
            else:
                if not cur.children[ord(word[i]) - 97]:
                    return False
                return dfs(i + 1,cur.children[ord(word[i]) - 97])
        return dfs(0, cu)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)