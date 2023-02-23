class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        nums = list(accumulate(nums))  
        nums = [num % k for num in nums] 
        count = Counter(nums)
        ans = 0
        for key, amount in count.items():
            if key % k == 0:
                ans += ((amount * (amount + 1))//2)
            else:
                ans += ((amount * (amount - 1))//2)
        return ans
            
        
        
        
        
        
       