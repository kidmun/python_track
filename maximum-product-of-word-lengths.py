class Solution:
    def maxProduct(self, words: List[str]) -> int:
        for i, w in enumerate(words):
            bit = 0
            for ch in w:
                bit |= (1<<(ord(ch) - 97))
            words[i] = (len(w), bit)
        words.sort()
        
        def checkCommonLetter(word1, word2):
            ma = max(word1,word2)
            ma = int(math.log(ma, 2)) + 1
            for i in range(ma):
                if (word1 & (1 << i)) and (word2 & (1 << i)):
                    return True
            return False
        right = len(words) - 1
        ans = 0
        while right > -1:
            left = right - 1
            while left > -1:
                if not checkCommonLetter(words[right][1], words[left][1]):
                    ans = max(words[right][0] *  words[left][0], ans)
                left -= 1
            right -= 1
        return ans