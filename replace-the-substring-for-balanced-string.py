class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        n = len(s)
        compare = {}
        for key, amount in count.items():
            if amount > n // 4:
                compare[key] =  amount - n // 4
        if len(compare) == 0:
            return 0
        left = 0
        window = Counter()
        ans = float("inf")
        def check(window, compare):
            for key, am in compare.items():
                if key not in window or window[key] < am:
                    return False
            return True
        for i, ch in enumerate(s):
            window[ch] += 1
            while check(window, compare) and left <= i: 
                ans = min(ans, i - left + 1)
                window[s[left]] -= 1
                left += 1
            
        return ans