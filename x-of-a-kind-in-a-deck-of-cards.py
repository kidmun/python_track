class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = list(Counter(deck).values())
        cur = count[0]
        for freq in count:
            cur = math.gcd(cur, freq)
        if cur > 1:
            return True
        return False