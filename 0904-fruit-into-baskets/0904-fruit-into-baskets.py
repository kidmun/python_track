class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        count = Counter()
        ans = 1
        for i, fruit in enumerate(fruits):
            count[fruit] += 1      
            if len(count) > 2 or i == (len(fruits) - 1):
                if len(count) > 2:
                    ans = max(ans, i - left)
                else:
                    ans = max(ans, i - left + 1)
                while len(count) > 2 and left < i:
                    count[fruits[left]] -= 1
                    if count[fruits[left]] == 0:
                        del count[fruits[left]]
                    left += 1
        return ans           
                
                
        