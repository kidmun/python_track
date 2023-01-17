class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            s = str(nums[i])
            m = len(s)
            flag = False
            val = ""
            for j in range(m - 1, -1, -1):
                if s[j] != 0 and (not flag):
                    flag = True
                    val += s[j]
                else:
                    if flag:
                        val += s[j]
                    
                        
            nums.append(int(val))
        return len(set(nums))
                    
                
                
            
            
            