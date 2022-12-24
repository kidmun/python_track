class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        index = 0
        n = len(words)
        while (index + 1) < n:
            for i in range(len(words[index])):
                if i == len(words[index + 1]):
                    return False
                ind1 = order.index(words[index][i])
                ind2 = order.index(words[index + 1][i])
                if ind1 < ind2:
                    break
                if ind1 > ind2:
                    return False
            index += 1
        return True