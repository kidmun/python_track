class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        for i, q in enumerate(queries):
            count = {}
            sm = q[0]
            for ch in q:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1
                if ord(ch) < ord(sm):
                    sm = ch
            queries[i] = count[sm]
        for i, w in enumerate(words):
            count = {}
            sm = w[0]
            for ch in w:
                if ch in count:
                    count[ch] += 1
                else:
                    count[ch] = 1
                if ord(ch) < ord(sm):
                    sm = ch
            words[i] = count[sm]
        words.sort()
   
        for i, q in enumerate(queries):
            
            left = 0
            right = len(words) - 1
            ans = 0
            while left <= right:
                mid = (left + right) // 2
                if words[mid] <= q:
                    left = mid + 1
                else:
                    ans = len(words) - mid
                    right = mid - 1
            queries[i] = ans
        return queries