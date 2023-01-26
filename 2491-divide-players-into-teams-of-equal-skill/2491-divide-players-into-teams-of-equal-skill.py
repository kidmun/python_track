class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        prev = skill[0] + skill[-1]
        flag = True
        res = skill[0] * skill[-1]
        left = 1
        right = n - 2
        while left < right:
            if (skill[left] + skill[right]) != prev:
                flag = False
                break
            res += skill[left] * skill[right]
            left += 1
            right -= 1
            
            
        if flag:
            return res
        else:
            return -1
                
            
        
        
        