class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        count = Counter(words)
        flag = False
        for w in count:
            if flag and count[w] % 2 and w[0] == w[1]:
                ans += (count[w] - 1) * 2
            else:
                ans += min(count[w], count[w[::-1]]) * 2
            if not flag and count[w] % 2 and w[0] == w[1]:
                flag = True
            # print(w, ans, flag)
        return ans 
    
    
        