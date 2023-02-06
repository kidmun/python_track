
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        maxx = sorted(list(set(height)),reverse = True)
        dic = defaultdict(int)
        for heg in height:
            dic[heg] += 1
        right = 0
        left = 0
        answer = 0
        for num in height:
            dic[num] -= 1
            while right < len(maxx) and dic[maxx[right]] == 0 :
                right += 1
            if right == len(maxx):
                return answer
            max_height = min(left,maxx[right])
            if max_height > num:
                answer += (max_height - num)
            if num > left:
                left = num
        return answer
                


                
                
                
            
        
  