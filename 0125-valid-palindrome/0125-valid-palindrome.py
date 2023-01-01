class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph_s = ""
        for char in s:
            if char.isalnum():
                alph_s += char.lower()
        left = 0
        right = len(alph_s) - 1
        while left <= right:
            if alph_s[left] != alph_s[right]:
                print(alph_s[left], alph_s[right])
                return False
            left += 1
            right -= 1
        return True
            
            
        