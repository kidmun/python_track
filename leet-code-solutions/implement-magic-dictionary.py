class MagicDictionary:

    def __init__(self):
        self.sett = set()
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.sett.add(word)

    
    def search(self, searchWord: str) -> bool:
   
        for i in range(len(searchWord)):
            for j in range(26):
                if searchWord[:i] + chr(97 + j) + searchWord[i + 1:] in self.sett and chr(97 + j) != searchWord[i]:
                    return True
        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)