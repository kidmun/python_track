class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        keys = sorted(count.keys())
        ans = []
        if count[0] % 2:
            return []
        for k in keys:
            while count[k] > 0:
                if count[k * 2] < 1:
                    return []
                ans.append(k)
                count[k] -= 1
                count[k * 2] -= 1
        return ans
                 

        